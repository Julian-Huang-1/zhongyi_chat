# -*- coding: utf-8 -*-
# @Time    : 2023/6/5 2:03
# @Author  : hjxylgogogo
# @File    : util.py
# @Software: PyCharm
from pprint import pprint

from typing import List
import openai
from qdrant_client import QdrantClient
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
)

openai.api_key = "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"
content = [{'role': 'system', 'content': '你是一擅长做阅读理解的助手'}]
user_content = []


def embedding(input:str):
    response = openai.Embedding.create(input=input,model="text-embedding-ada-002")
    return response["data"][0]["embedding"]

@retry(wait=wait_random_exponential(min=1, max=5), stop=stop_after_attempt(4))
def LLM(prompt:List[dict]):
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=prompt,temperature=0)
    return response["choices"][0]["message"]

def decorated(input:str):
    input = {"role": "user", "content": input}
    return input

def review_qusetion(input:str):
    print("content:")
    pprint(content)
    user_content.append(decorated(input))
    review_prompt = "下面这句话与中草药、中医相关吗？回答yes或no\\n"+input
    review_prompt = [decorated(review_prompt)]
    res = LLM(review_prompt)
    if res["content"] =="yes":
        res=zhongyi_chat(decorated(input))
    else:
        res=chat(decorated(input))
    print(res)
    return res

def zhongyi_chat(input:dict):
    client = QdrantClient(":memory:")
    client = QdrantClient(path="path/to/db")
    q_v = embedding(input["content"])
    hits = client.search(
        collection_name="zhongyi_collection",
        query_vector=q_v,
        limit=5  # Return 5 closest points
    )
    if hits[0].score>0.8:
        input["content"] = "请做阅读理解:\\n" + hits[0].payload["content"] + "\\n问：" + input["content"] + "\\n答："
        content.append(input)
    else:
        pass
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

def search_api():
    pass