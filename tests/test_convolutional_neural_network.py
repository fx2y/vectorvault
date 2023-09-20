import unittest

from feature_extraction import ConvolutionalNeuralNetwork


class TestConvolutionalNeuralNetwork(unittest.TestCase):
    def setUp(self):
        self.cnn = ConvolutionalNeuralNetwork()

    def test_extract(self):
        # Test with a sample image
        with open("../resources/test_image.jpg", "rb") as f:
            image_data = f.read()
        features = self.cnn.extract(image_data)
        self.assertEqual(len(features), 25088)
        self.assertIsInstance(features, list)
        self.assertIsInstance(features[0], float)

        # Test with a different image
        with open("../resources/test_image2.jpg", "rb") as f:
            image_data = f.read()
        features2 = self.cnn.extract(image_data)
        self.assertNotEqual(features, features2)


if __name__ == '__main__':
    unittest.main()
