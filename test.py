# -*- coding: utf-8 -*-
# @Time    : 2023/6/5 1:37
# @Author  : hjxylgogogo
# @File    : test.py.py
# @Software: PyCharm
from util import *
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams
from qdrant_client import QdrantClient

client = QdrantClient(":memory:")
client = QdrantClient(path="path/to/db")  # Persists changes to disk
collection_info = client.get_collection(collection_name="image_collection")

###删除表
# client.delete_collection("zhongyi_collection")

###查看表内容
# query_vector = embedding("方剂")
query_vector = image_embedding("path/to/images/3.jpg")
hits = client.search(
    collection_name="image_collection",
    query_vector=query_vector,
    limit=20  # Return 5 closest points
)
pass
