from src.connector.MongoDB import MongoDBConnector
from typing import Any
from faker import Faker


class DocSeeder:
    def __init__(
        self, connector: MongoDBConnector, schema: dict[str, "EntrySeeder"]
    ) -> None:
        self.connector = connector
        self.schema = schema

    def seed(self) -> dict:
        return {k: v.seed() for k, v in self.schema.items()}


class EntrySeeder:
    def __init__(self, type: "str | list | DocSeeder", optional: bool = False) -> None:
        self.type = type
        self.optional = optional
        self.__fake = Faker("it_IT")

    def seed(self) -> Any:
        if isinstance(self.type, DocSeeder):
            return self.type.seed()
        elif isinstance(self.type, list):
            return self.__fake.random_element(self.type)
        else:
            return self.__fake.__getattr__(self.type)()
