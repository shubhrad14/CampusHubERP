from datetime import datetime
from abc import ABCMeta


class ModelMeta(ABCMeta):
    def __new__(cls, name, bases, namespace):
        namespace["created_at"] = None
        namespace["updated_at"] = None

        return super().__new__(cls, name, bases, namespace)


class BaseModel(metaclass=ModelMeta):
    def __init__(self):
        current_time = datetime.now()

        self.created_at = current_time
        self.updated_at = current_time

    def update_timestamp(self):
        self.updated_at = datetime.now()