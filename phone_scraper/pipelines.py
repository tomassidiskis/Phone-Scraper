Python 3.11.5 (v3.11.5:cce6ba91b3, Aug 24 2023, 10:50:31) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> from pymongo import MongoClient
... 
... class MongoDBPipeline:
...     def __init__(self, mongo_server, mongo_port, mongo_db, mongo_collection):
...         self.mongo_server = mongo_server
...         self.mongo_port = mongo_port
...         self.mongo_db = mongo_db
...         self.mongo_collection = mongo_collection
... 
...     @classmethod
...     def from_crawler(cls, crawler):
...         return cls(
...             mongo_server=crawler.settings.get('MONGODB_SERVER'),
...             mongo_port=crawler.settings.get('MONGODB_PORT'),
...             mongo_db=crawler.settings.get('MONGODB_DB'),
...             mongo_collection=crawler.settings.get('MONGODB_COLLECTION')
...         )
... 
...     def open_spider(self, spider):
...         self.client = MongoClient(self.mongo_server, self.mongo_port)
...         self.db = self.client[self.mongo_db]
... 
...     def close_spider(self, spider):
...         self.client.close()
... 
...     def process_item(self, item, spider):
...         self.db[self.mongo_collection].insert_one(dict(item))
...         return item
