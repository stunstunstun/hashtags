from pymongo import MongoClient


class MongoDB:
    def __init__(self, uri):
        self.db = MongoClient(uri, maxPoolSize=10).get_database()