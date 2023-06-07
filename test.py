# -*- coding: utf-8 -*-
# @Time    : 2023/6/5 1:37
# @Author  : hjxylgogogo
# @File    : test.py.py
# @Software: PyCharm
from util import *
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams
client = QdrantClient(url="127.0.0.1:8082")
client.recreate_collection(
    collection_name="test_collection",
    vectors_config=VectorParams(size=4, distance=Distance.DOT),
)
pass
