from pymongo import MongoClient

class MongoDBConnector:
  def __init__(self, db,url="mongodb://localhost:27017/") -> None:
    self.__client = MongoClient(url)
    self.db = self.__client[db]
   
  @property
  def collections(self)->list[str]:
    return self.db.list_collection_names()
  
  def infer_schema(self,collection, sample_size=100):
    fields = set()
    for doc in self.db[collection].find({}, projection=None).limit(sample_size):
        fields.update(doc.keys())
    return sorted(fields)