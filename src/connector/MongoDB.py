from pymongo import MongoClient
from src.utils import cprint


class MongoDBConnector:
    def __init__(self, db, url="mongodb://localhost:27017/") -> None:
        self.db_name = db
        self.__client = MongoClient(url)
        self.db = self.__client[db]
        self.stats()

    @property
    def collections(self) -> list[str]:
        return self.db.list_collection_names()

    def infer_schema(self, collection, sample_size=100):
        fields = set()
        for doc in self.db[collection].find({}, projection=None).limit(sample_size):
            fields.update(doc.keys())
        return sorted(fields)

    def stats(self) -> None:
        cprint(f"The collections of the", f"yellow:{self.db_name}", "db are:")
        print("-" * 40)
        for collection in sorted(self.collections):
            schema = self.infer_schema(collection)
            cprint(f"[{collection}]:", *[f"rand:{_}" for _ in schema])
