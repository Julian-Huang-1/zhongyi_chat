# -*- coding: utf-8 -*-
# @Time    : 2023/6/6 1:00
# @Author  : hjxylgogogo
# @File    : run.py
# @Software: PyCharm
import uvicorn
import util
from fastapi import FastAPI
from pydantic import BaseModel

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 允许所有域的跨域请求
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    q:str

@app.post("/chat/")
def chatgpt(item:Item):
    print("收到"+item.q)
    return util.review_qusetion(item.q)
    # return item.q

@app.get("/chat")
def new_chat():
    util.content = [{'role': 'system', 'content': '你是一擅长做阅读理解的助手'}]
    util.user_content = []
    return "ok"
##
if __name__ == "__main__":
    while True:
        x = input("q:")
        util.review_qusetion(x)





