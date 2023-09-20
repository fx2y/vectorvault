import io
from abc import ABC, abstractmethod
from typing import List

import tensorflow as tf
from PIL import Image
from keras.applications.vgg16 import preprocess_input
from keras.preprocessing import image


class FeatureExtractor(ABC):
    @abstractmethod
    def extract(self, data: bytes) -> List[float]:
        pass


class ConvolutionalNeuralNetwork(FeatureExtractor):
    def __init__(self):
        self.model = tf.keras.applications.VGG16(weights='imagenet', include_top=False)

    def extract(self, data: bytes) -> List[float]:
        try:
            img = Image.open(io.BytesIO(data)).convert('RGB')
        except (OSError, ValueError):
            # Invalid image data
            return []
        if img.size != (224, 224):
            img = img.resize((224, 224))
        x = image.img_to_array(img)
        x = preprocess_input(x)
        features = self.model.predict(tf.expand_dims(x, axis=0))
        return features.flatten().tolist()


class RecurrentNeuralNetwork(FeatureExtractor):
    def extract(self, data: bytes) -> List[float]:
        # implementation for extracting features from videos using RNN
        pass
