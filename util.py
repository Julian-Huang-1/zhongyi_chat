# -*- coding: utf-8 -*-
# @Time    : 2023/6/5 2:03
# @Author  : hjxylgogogo
# @File    : util.py
# @Software: PyCharm
import openai

def embedding(input:str):
    openai.api_key = "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"
    response = openai.Embedding.create(input=input,model="text-embedding-ada-002")
    return response["data"][0]["embedding"]

def LLM(input:str):
    pass