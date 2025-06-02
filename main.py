from fastapi import FastAPI
from fastapi.responses import FileResponse
from typing import Union
from pydantic import BaseModel

from const.kakao_conversation import KakaoConversaionId, MajorCode
from model.major import Major
import requests
app = FastAPI()

headers = {
        'Authorization': 'Bearer e0530d2e.12f54b7fdb1f4628a6280c34eee7ef0c',
        'Content-Type': 'application/json'
}

@app.get("/users/kakao")
def get_kakao_users():
    res = requests.get("https://api.kakaowork.com/v1/users.list", headers=headers)
    result = res.json()
    return result["users"]

@app.get("/room/invite")
def invite_room():
    users = get_kakao_users()
    response = []
    for user in users:
      print(user["name"], user["department"])
      if(MajorCode.get(user["department"]) == None): continue
      print(user["name"], MajorCode.get(user["department"]),KakaoConversaionId[MajorCode.get(user["department"])].value)
      data = {
          'user_ids': [user["id"]]
      }
      res = requests.post(f"https://api.kakaowork.com/v1/conversations/{KakaoConversaionId[MajorCode.get(user["department"])].value}/invite", headers=headers, json=data)
      result = res.json()
      response.append(result)
    return response

class KickUser(BaseModel):
    conversation_id: int
    user_ids: list[int]
@app.delete("/room/kick")
def kick_room(body: KickUser):
    data = {
        'user_ids': body.user_ids
    }
    res = requests.post(f"https://api.kakaowork.com/v1/conversations/{body.conversation_id}/kick", headers=headers, json=data)
    result = res.json()
    return result

@app.get("/conversation")
def make_chat():
    data = {
        'user_ids': [],
        'conversation_name': "빈채팅방"
    }
    res = requests.post("https://api.kakaowork.com/v1/conversations.open", headers=headers, json=data)
    result = res.json()
    return result


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