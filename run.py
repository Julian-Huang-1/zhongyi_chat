# -*- coding: utf-8 -*-
# @Time    : 2023/6/6 1:00
# @Author  : hjxylgogogo
# @File    : run.py
# @Software: PyCharm
import uvicorn
import util
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    q:str

@app.post("/chat/")
async def chatgpt(item:Item):
    return util.review_qusetion(item.q)
    # return item.q

@app.get("/chat")
async def new_chat():
    util.content = [{'role': 'system', 'content': '你是一擅长做阅读理解的助手'}]
    util.user_content = []
    return "ok"
##
if __name__ == "__main__":
    while True:
        x = input("q:")
        util.review_qusetion(x)





