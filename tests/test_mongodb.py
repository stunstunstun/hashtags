# -*- coding: utf-8 -*-
import unittest

from hashtags.mongodb import MongoDB
from hashtags.constants import MONGO_URI


class TestMongoDB(unittest.TestCase):

    def setUp(self):
        self.client = MongoDB(MONGO_URI)
    
    def test_collections(self):
        collections = self.client.db.list_collection_names()
        self.assertTrue(isinstance(collections, list))
