# -*- coding: utf-8 -*-
# @Time    : 2023/6/5 1:37
# @Author  : hjxylgogogo
# @File    : test.py.py
# @Software: PyCharm
from util import *
from qdrant_client import QdrantClient
client = QdrantClient(":memory:")
client = QdrantClient(path="path/to/db")
collection_info = client.get_collection(collection_name="zhongyi_collection")
q ="有一种方剂叫做阳和汤。这个中药方子的作用是什么？"
q_v = embedding(q)

hits = client.search(
    collection_name="zhongyi_collection",
    query_vector=q_v,
    limit=5  # Return 5 closest points
)
pass