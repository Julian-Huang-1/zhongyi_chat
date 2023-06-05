# -*- coding: utf-8 -*-
# @Time    : 2023/6/5 2:03
# @Author  : hjxylgogogo
# @File    : util.py
# @Software: PyCharm
from typing import List

import openai
from qdrant_client import QdrantClient
openai.api_key = "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"
content = []
user_content = []
client = QdrantClient(":memory:")
client = QdrantClient(path="path/to/db")
def embedding(input:str):
    response = openai.Embedding.create(input=input,model="text-embedding-ada-002")
    return response["data"][0]["embedding"]

def LLM(prompt:List[dict]):
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=prompt)
    return response["choices"][0]["message"]

def decorated(input:str):
    input = {"role": "user", "content": input}
    return input


def review_qusetion(input:str):
    user_content.append(decorated(input))
    review_prompt = "下面这句话与中医相关吗？回答yes或no\\n"+input
    review_prompt = [decorated(review_prompt)]
    res = LLM(review_prompt)
    if res["content"] =="yes":
        res=zhongyi_chat(decorated(input))
    else:
        res=chat(decorated(input))
    print(res)

def zhongyi_chat(input:dict):
    q_v = embedding(input["content"])
    hits = client.search(
        collection_name="zhongyi_collection",
        query_vector=q_v,
        limit=5  # Return 5 closest points
    )
    input["content"] = "请做阅读理解:\\n"+hits[0].payload["content"]+"\\n问："+ input["content"]+"\\n答："
    content.append(input)
    res = LLM(content)
    content.append(res.to_dict())
    user_content.append(res.to_dict())
    return res["content"]


def chat(input:dict):
    input["content"] =  input["content"] +",请用中文回答"
    content.append(input)
    res =LLM(content)
    content.append(res.to_dict())
    user_content.append(res.to_dict())
    return res["content"]