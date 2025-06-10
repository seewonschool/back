from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import requests
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
#ActionChains모듈 가져오기
from selenium.webdriver import ActionChains



load_dotenv()

kakao_token = os.getenv("MY_KAKAO_TOKEN", "")
kakao_password = os.getenv("MY_KAKAO_PW", "")

headers = {
    'Authorization': 'Bearer e0530d2e.12f54b7fdb1f4628a6280c34eee7ef0c',
    'Content-Type': 'application/json'
}

while True:
    # Selenium options
    chrome_options = webdriver.ChromeOptions()
    ua = UserAgent()
    userAgent = ua.random
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument(f"user-agent={userAgent}")

    # 웹드라이버 설정
    # service = Service("/usr/bin/chromedriver")  # 직접 경로 명시
    # driver = webdriver.Chrome(options=chrome_options)
    # driver = webdriver.Chrome()
    driver = webdriver.Chrome(
      service=Service(ChromeDriverManager().install()), 
      options=chrome_options
    )

    driver.implicitly_wait(20)
    # 로그인 페이지로 이동
    driver.get('https://kakaowork.com/login?service=admin')

    # 로컬 스토리지에 값 설정
    script = f"""
    window.localStorage.setItem('kakaowork.com_auth_token', '{kakao_token}');
    """
    driver.execute_script(script)

    # 페이지 새로고침하여 로컬 스토리지 값 반영
    driver.refresh()
    driver.implicitly_wait(100)

    # 서강대학교 공지알리미 버튼 클릭
    btn1 = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/ul/li[2]/a')
    btn1.click()
    driver.implicitly_wait(100)


    ############# login page ##############
    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys(kakao_password)

    # 로그인 버튼 클릭
    login_button = driver.find_element(By.ID, 'btn-login')
    login_button.click()

    # 페이지 로딩을 기다림 (필요 시 시간 조정)
    driver.implicitly_wait(100)

    # 멤버 관리 버튼
    btn2 = driver.find_element(By.XPATH, '/html/body/div/main/section/div[1]/nav/ul/li[2]/strong')
    btn2.click()
    driver.implicitly_wait(100)

    ##### 멤버 정보 등록
    # firebase 계정 키 파일 경로
    cred = credentials.Certificate("firebasekey.json")
    firebase_admin.initialize_app(cred)
    # Firestore 클라이언트 초기화
    db = firestore.client()
    students_ref = db.collection('students')
    docs = students_ref.stream()

    # 등록된 "~대학" 의 +버튼 path 전부 추가 (전부 열고 선택하는 방식으로)
    parent_major_path = {
        "소프트웨어융합대학": "/html/body/div[5]/div/div/section/div[2]/div[1]/div/div/div/div/div[2]/div/div/button",
        "공과대학": "/html/body/div[5]/div/div/section/div[2]/div[1]/div/div/div/div/div[3]/div/div/button",
        "인문대학": "/html/body/div[5]/div/div/section/div[2]/div[1]/div/div/div/div/div[4]/div/div/button",
        "지식융합미디어대학": "/html/body/div[5]/div/div/section/div[2]/div[1]/div/div/div/div/div[5]/div/div/button",
        "자연과학대학": "/html/body/div[5]/div/div/section/div[2]/div[1]/div/div/div/div/div[6]/div/div/button"
    }

    # 과별 버튼 path
    child_major_path = {
        "컴퓨터공학과": "/html/body/div[5]/div/div/section/div[2]/div[1]/div/div/div/div/div[3]",
        "인공지능학과": "/html/body/div[5]/div/div/section/div[2]/div[1]/div/div/div/div/div[4]/div/div/div/div/div[4]/div/div[2]/span/div",
        "AI기반 자유전공학부": "/html/body/div[5]/div/div/section/div[2]/div[1]/div/div/div/div/div[5]/div/div/div/div/div[4]/div/div[2]/span/div",
        "전자공학과": "/html/body/div[5]/div/div/section/div[2]/div[1]/div/div/div/div/div[4]/div/div/div/div/div[4]/div/div[2]/span/div",
        "화공생명공학과": "/html/body/div[5]/div/div/section/div[2]/div[1]/div/div/div/div/div[5]/div/div/div/div/div[4]/div/div[2]/span/div",
        "기계공학과": "/html/body/div[5]/div/div/section/div[2]/div[1]/div/div/div/div/div[6]/div/div/div/div/div[4]/div/div[2]/span/div",
        "시스템반도체공학과": "/html/body/div[5]/div/div/section/div[2]/div[1]/div/div/div/div/div[7]/div/div/div/div/div[4]/div/div[2]/span/div",
        "국어국문학과": "/html/body/div[5]/div/div/section/div[2]/div[1]/div/div/div/div/div[5]/div/div/div/div/div[4]/div/div[2]/span/div",
        "영문학부": "/html/body/div[5]/div/div/section/div[2]/div[1]/div/div/div/div/div[6]/div/div/div/div/div[4]/div/div[2]/span/div",
        "미디어&엔터테인먼트학과": "/html/body/div[5]/div/div/section/div[2]/div[1]/div/div/div/div/div[6]/div/div/div/div/div[4]/div/div[2]/span/div",
        "수학과": "/html/body/div[5]/div/div/section/div[2]/div[1]/div/div/div/div/div[7]/div/div/div/div/div[4]/div/div[2]/span/div"
    }

    #firebase 내 유저 정보 카카오에 등록
    for doc in docs :
        # 멤버 등록 버튼
        btn3 = driver.find_element(By.XPATH, '/html/body/div/main/section/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/button[3]')
        btn3.click()
        driver.implicitly_wait(100)

        row = {"id": doc.id, **doc.to_dict()}
        # id(이메일)
        driver.find_element(By.XPATH, '/html/body/div[4]/div/div/section/form/div[1]/fieldset[1]/div[1]/div/div/div/input').send_keys(row.get("email", ""))

        # 이름
        driver.find_element(By.XPATH, '/html/body/div[4]/div/div/section/form/div[1]/fieldset[1]/div[3]/div/div/input').send_keys(row.get("name", ""))

        # 소속 버튼
        major_btn1 = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/section/form/div[1]/fieldset[2]/div[1]/div/div/div/button')
        major_btn1.click()
        major_btn1.click() #안눌려서 일부러 2번 넣은거임
        driver.implicitly_wait(30)

        # 조직 선택 버튼
        major_btn2 = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/section/form/div[1]/fieldset[2]/div[1]/div/div/div[1]/div/div[2]/input')
        major_btn2.click()
        driver.implicitly_wait(30)

        # 유저 소속 버튼
        user_major = (row.get("major")).split("|")
        print(user_major)

        # 자기 대학 버튼만 열고
        major_btn3 = driver.find_element(By.XPATH, parent_major_path.get(user_major[1]))
        major_btn3.click()
        driver.implicitly_wait(50)

        # 대학 버튼 전부 열기
        # major_container = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/section/div[2]/div[1]/div/div')
        # for path in parent_major_path:
        #     print(path)
        #     major_btn3 = driver.find_element(By.XPATH, path)
        #     # driver.execute_script("arguments[0].scrollBy(0, 50%)", major_container) #스크롤을 해야지만.. 클릭할 수 있는 것 같다..
        #     print(major_btn3)
        #     driver.execute_script("arguments[0].scrollTop = arguments[0].scrollTop + arguments[1];", major_container, 338)
        #     #move_to_element를 이용하여 이동
        #     action.move_to_element(major_btn3).perform()
        #     major_btn3.click()
        #     driver.implicitly_wait(50)

        

        print(child_major_path.get(user_major[2]))
        major_btn = driver.find_element(By.XPATH, child_major_path.get(user_major[2]))
        major_btn.click()
        driver.implicitly_wait(100)

        # # 소속 등록 확인 버튼
        major_ok = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/section/div[3]/button[2]')
        major_ok.click()
        driver.implicitly_wait(100)

        # input("되나")

        #등록 버튼
        driver.find_element(By.XPATH, '/html/body/div[3]/div/div/section/form/div[2]/button[2]').click()

        #등록 완료 팝업 확인 버튼
        driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[3]/button').click()

        # 등록한 유저 정보 firebase에서 삭제
        # doc.reference.delete()
    driver.quit()

    time.sleep(60)
    res = requests.get('http://127.0.0.1:8000/room/invite', headers=headers)

    time.sleep(300) #5분 뒤 재실행









