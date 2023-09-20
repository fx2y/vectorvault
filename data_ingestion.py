import os
from abc import ABC, abstractmethod
from typing import List, Dict


class DataReader(ABC):
    @abstractmethod
    def read(self, source: str) -> List[Dict]:
        pass


class FileSystemReader(DataReader):
    def read(self, source: str) -> List[Dict]:
        if not source.startswith("file:"):
            raise ValueError("Invalid source format. Must start with 'file:'")
        path = source[5:]
        if not os.path.isfile(path):
            raise ValueError(f"File not found: {path}")
        with open(path, "r") as f:
            lines = f.readlines()
        data = []
        for line in lines:
            # parse line and convert to dictionary
            # assuming format: "key1=value1,key2=value2,..."
            pairs = line.strip().split(",")
            d = {}
            for pair in pairs:
                key, value = pair.split("=")
                d[key] = value
            data.append(d)
        return data


class CloudStorageReader(DataReader):
    def read(self, source: str) -> List[Dict]:
        # implementation for reading from cloud storage
        pass


class DatabaseReader(DataReader):
    def read(self, source: str) -> List[Dict]:
        # implementation for reading from database
        pass


class DataIngester:
    def __init__(self, readers: Dict[str, DataReader]):
        self.readers = readers

    def ingest(self, source: str) -> List[Dict]:
        reader_type = source.split(":")[0]
        reader = self.readers.get(reader_type)
        if reader is None:
            raise ValueError(f"No reader found for source {source}")
        return reader.read(source)
