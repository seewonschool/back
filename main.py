from typing import Union
from pydantic import BaseModel

from fastapi import FastAPI

app = FastAPI()

from model.major import Major
import requests

headers = {
        'Authorization': 'Bearer e0530d2e.12f54b7fdb1f4628a6280c34eee7ef0c',
        'Content-Type': 'application/json'
}

@app.get("/conversation")
def make_chat():
    data = {
        'user_ids': [],
        'conversation_name': "빈채팅방"
    }
    res = requests.post("https://api.kakaowork.com/v1/conversations.open", headers=headers, json=data)
    result = res.json()
    print(result)

class Msg(BaseModel):
    conversation_id: int
    title: str
    date: str
    link: str

@app.post("/chat", summary="채팅 전송")
def send_chat(msg: Msg):
    data = {
            "conversation_id": msg.conversation_id,
            "text": msg.title,
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
    res = requests.post("https://api.kakaowork.com/v1/messages.send", headers=headers, json=data)
    result = res.json()
    return result