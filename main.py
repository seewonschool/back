from typing import Union
from pydantic import BaseModel

from fastapi import FastAPI

app = FastAPI()

from model.major import Major
import requests

import firebase_admin
from firebase_admin import credentials

# 서비스 계정 키 파일 경로
cred = credentials.Certificate("firebasekey.json")
firebase_admin.initialize_app(cred)

from firebase_admin import firestore
from fastapi.responses import FileResponse

# Firestore 클라이언트 초기화
db = firestore.client()

from openpyxl import Workbook


headers = {
        'Authorization': 'Bearer e0530d2e.12f54b7fdb1f4628a6280c34eee7ef0c',
        'Content-Type': 'application/json'
}

@app.get("/students")
def get_students_collection():
    # 'students' 컬렉션의 모든 문서 가져오기
    students_ref = db.collection('students')
    docs = students_ref.stream()

    # 문서 데이터 추출 -> 엑셀을 만들어서 -> 삭제 -> 등록 -> 초대
    # students = [doc.to_dict() for doc in docs]
    # data = [{"id": doc.id, **doc.to_dict()} for doc in docs]

    # 2. 엑셀 파일 생성
    wb = Workbook()  # 새 엑셀 파일 생성
    ws = wb.active   # 기본 워크시트 선택
    ws.title = "Students Data"  # 워크시트 이름 설정

    # 데이터 헤더 추가
    headers = [ "ID(이메일)*",
                "이름*",
                "닉네임",
                "조직",
                "직책",
                "직위",
                "휴대전화",
                "유선전화",
                "이메일",
                "근무위치",
                "생일",
                "상태 메세지"]  # 각 필드에 맞는 헤더 설정
    ws.append(headers)  # 첫 번째 행에 헤더 추가

    for doc in docs :
      row = {"id": doc.id, **doc.to_dict()}
      # 데이터 추가
      ws.append([row.get("email", ""), row.get("name", ""), "", row.get("major", ""),"", "","","",row.get("email", ""),"", "", ""])
      # doc.reference.delete()
      

    # 3. 파일 저장 경로 설정
    file_name = "students_data.xlsx"
    wb.save(file_name)  # 엑셀 파일 저장

    students_ref_re = db.collection('students')
    docs_re = students_ref_re.stream()
    for doc in docs_re:
        doc.reference.delete()
    
    # 4. 파일 응답 반환
    return FileResponse(file_name, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", filename=file_name)

    # return students



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