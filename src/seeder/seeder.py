from random import random
from src.connector.MongoDB import MongoDBConnector
from typing import Any, Callable
from faker import Faker


class DocSeeder:
    def __init__(self, schema: dict[str, "EntrySeeder"]) -> None:
        self.schema = schema

    def __seed(self) -> dict:
        return {
            k: v
            for k, v in {k: v.seed() for k, v in self.schema.items()}.items()
            if v != None
        }

    def seed(self, amount: int | None = None) -> dict | list[dict]:
        return (
            self.__seed() if amount is None else [self.__seed() for _ in range(amount)]
        )


class EntrySeeder:
    def __init__(
        self,
        type: "str | list|range | DocSeeder | Callable[[Faker],Any]",
        p: float = 1,
        unique: bool = False,
    ) -> None:
        self.type = type
        self.p = p
        self.__fake = Faker("it_IT")
        self.unique = unique
        if unique:
            assert isinstance(type, (list, range))
            self.counter = 0

    def seed(self) -> Any:
        if random() > self.p:
            return None
        if isinstance(self.type, DocSeeder):
            return self.type.seed()
        elif isinstance(self.type, Callable):
            return self.type(self.__fake)
        elif isinstance(self.type, (list, range)):
            self.type = list(self.type)
            if self.unique:
                if self.counter >= len(self.type):
                    raise Exception("No more values")
                val = self.type[self.counter]
                self.counter += 1
                return val
            return self.__fake.random_element(self.type)
        else:
            return self.__fake.__getattr__(self.type)()
