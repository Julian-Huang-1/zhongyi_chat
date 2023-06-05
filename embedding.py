# -*- coding: utf-8 -*-
# @Time    : 2023/6/5 0:17
# @Author  : hjxylgogogo
# @File    : embedding.py
# @Software: PyCharm
import openai


# Provide OpenAI API key and choose one of the available models:
# https://beta.openai.com/docs/models/overview
openai.api_key = "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"
embedding_model = "text-embedding-ada-002"

with open("test.txt","r",encoding='utf-8')as f:
    f.readline()
    data =[i for i in f]

vectors=[]
for s in data:
    response = openai.Embedding.create(
        input=s,
        model=embedding_model
    )
    vectors.append(response["data"][0]["embedding"])

from qdrant_client import QdrantClient
client = QdrantClient(":memory:")
client = QdrantClient(path="path/to/db")  # Persists changes to disk
from qdrant_client.models import Distance, VectorParams
client.recreate_collection(
    collection_name="zhongyi_collection",
    vectors_config=VectorParams(size=1536, distance=Distance.COSINE),
)

pass
from qdrant_client.models import PointStruct
client.upsert(
    collection_name="zhongyi_collection",
    points=[
        PointStruct(
            id=idx,
            vector=item[0],
            payload={"content": item[1]}
        )
        for idx, item in enumerate(zip(vectors,data))
    ]
)


pass