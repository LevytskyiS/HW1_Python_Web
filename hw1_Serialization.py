from abc import ABC, abstractmethod
import pickle
import json

class SerializationInterface(ABC):
    
    @abstractmethod
    def serialize_container(self, data):
        pass


class SerializationToBin(SerializationInterface):
    
    def serialize_container(self, data):
        with open('bin_file.bin', 'wb') as file:
                pickle.dump(data, file)


class SerializationToJson(SerializationInterface):
    
    def serialize_container(self, data):
        with open('json_file.json', 'wb') as file:
                json.dump(data, file)