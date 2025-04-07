import requests
import sys
import os
import time
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

headers = {
    'Authorization': 'Bearer e0530d2e.12f54b7fdb1f4628a6280c34eee7ef0c',
    'Content-Type': 'application/json'
}

detecting_interval = 30 #나중에 바꾸기

def crawling_main(file_path, conversation_id, craw_func):
  try:
      # 반복 실행
      while True:
          with open(file_path, "r") as json_file:
              old_data = json.load(json_file)

          notices = craw_func()
          print("크롤링 완료")

          print(notices)

          for item in notices:
              data_to_send = {
                      'conversation_id': conversation_id,
                      'date': item["date"],
                      'link': item["link"],
                      'title': item["title"]
                  }

              if not any(existing_item['title'] == item["title"] for existing_item in old_data):
                  # 해당 제목이 없다면 POST 요청 보내기
                  print("보내짐", item["title"])
                  res = requests.post('http://127.0.0.1:8000/chat', headers=headers, json=data_to_send)
                  if res.status_code == 200:
                      # 요청이 성공하면 데이터를 기존 리스트에 추가
                      old_data.append(data_to_send)
                      print(f"메세지 전송 완료: {item['title']}")
          
          # 업데이트된 데이터를 JSON 파일에 저장
          with open(file_path, "w") as json_file:
              json.dump(old_data, json_file, indent=4)

          time.sleep(detecting_interval) #1분 뒤 재실행

  finally:
      print("끝")