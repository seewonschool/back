from typing import Union
from pydantic import BaseModel

from fastapi import FastAPI

app = FastAPI()

from model.major import Major
import requests

from cse.important import cse_important
from kor.main import kor_important
from mec.main import MEC_important
from AI.main import AI_important
from AIE.main import AIE_important
from SSE.main import SSE_important
from CBE.main import CBE_important
from EE.main import EE_important

headers = {
        'Authorization': 'Bearer e0530d2e.12f54b7fdb1f4628a6280c34eee7ef0c',
        'Content-Type': 'application/json'
        }

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/notices/all/{major}")
def read_notice(major: Major):
    if major == Major.cse:
      
    #   res = requests.get('https://api.kakaowork.com/v1/users.list', headers=headers)
    #   result = res.json()
    #   print(result["users"])

      notices = cse_important()
      for item in notices:
          data = {
              'conversation_id': 12352747,
              'date': item["date"],
              'link': item["link"],
              'title': item["title"]
          }

          res = requests.post(f'http://127.0.0.1:8000/chat', headers=headers, json=data)

      return cse_important()
    if major == Major.kor:
        return kor_important()
    if major == "MEC":
        notices = MEC_important()
        for item in notices:
          data = {
              'conversation_id': 12352843,
              'date': item["date"],
              'link': item["link"],
              'title': item["title"]
          }

          res = requests.post(f'http://127.0.0.1:8000/chat', headers=headers, json=data)
        return MEC_important()
    if major == "AI":
        notices = AI_important()
        for item in notices:
          data = {
              'conversation_id': 12352747,
              'date': item["date"],
              'link': item["link"],
              'title': item["title"]
          }

          res = requests.post(f'http://127.0.0.1:8000/chat', headers=headers, json=data)
        return notices
    if major == "AIE":
        return AIE_important()
    if major == "SSE":
        return SSE_important()
    if major == "CBE":
        return CBE_important()
    if major == "EE":
        return EE_important()

@app.get("/conversation")
def make_chat():
    data = {
        'user_ids': [],
        'conversation_name': "빈채팅방"
    }
    res = requests.post("https://api.kakaowork.com/v1/conversations.open", headers=headers, json=data)
    result = res.json()
    print(result)

#"12352747"

import pyshorteners as ps

class Msg(BaseModel):
    conversation_id: int
    title: str
    date: str
    link: str

@app.post("/chat")
def send_chat(msg: Msg):
    sh = ps.Shortener()

    data = {"conversation_id":msg.conversation_id,
            "text":msg.title,
            "blocks":[
                {
      "type": "header",
      "text": "공지사항",
      "style": "yellow"
    },
    {
      "type": "text",
      "text": "text sample",
      "inlines": [
        {
          "type": "styled",
          "text": msg.title,
          "bold": True
        }
      ]
    },
    {
      "type": "description",
      "term": "등록일",
      "content": {
        "type": "text",
        "text": msg.date
      },
      "accent": True
    },
    {
      "type": "button",
      "text": "바로가기",
      "style": "default",
      "action": {
        "type": "open_system_browser",
        "name": "button1",
        "value": msg.link
      }
    }
        ]}
    print(data)
    res = requests.post("https://api.kakaowork.com/v1/messages.send", headers=headers, json=data)
    result = res.json()
    print(result)