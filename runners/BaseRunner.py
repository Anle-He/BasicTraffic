from abc import ABC, abstractmethod


class BaseRunner(ABC):
    
    @abstractmethod
    def train_one_epoch(self):
        pass


    @abstractmethod
    def train_model(self):
        pass


    @abstractmethod
    def eval_model(self):
        pass


    @abstractmethod
    def test_model(self):
        pass


    @abstractmethod
    def predict(self):
        pass


    @abstractmethod
    def model_summary(self):
        pass