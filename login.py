from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv

load_dotenv()

kakao_token = os.getenv("MY_KAKAO_TOKEN", "")
kakao_password = os.getenv("MY_KAKAO_PW", "")

# 웹드라이버 설정
driver = webdriver.Chrome()

# 로그인 페이지로 이동
driver.get('https://kakaowork.com/login?service=admin')

# 로컬 스토리지에 값 설정
script = f"""
window.localStorage.setItem('kakaowork.com_auth_token', '{kakao_token}');
"""
driver.execute_script(script)

# 페이지 새로고침하여 로컬 스토리지 값 반영
driver.refresh()
driver.implicitly_wait(30)

# 서강대학교 공지알리미 버튼 클릭
btn1 = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/ul/li[2]/a')
btn1.click()
driver.implicitly_wait(30)


############# login page ##############
password_field = driver.find_element(By.ID, 'password')
password_field.send_keys(kakao_password)

# 로그인 버튼 클릭
login_button = driver.find_element(By.ID, 'btn-login')
login_button.click()

# 페이지 로딩을 기다림 (필요 시 시간 조정)
driver.implicitly_wait(30)

# 로그인 후 작업 수행 가능
# 예: 데이터를 스크래핑하거나 특정 페이지로 이동

# 멤버 관리 버튼
btn2 = driver.find_element(By.XPATH, '/html/body/div/main/section/div[1]/nav/ul/li[2]/strong')
btn2.click()
driver.implicitly_wait(30)


# 멤버 일괄 등록 버튼
btn3 = driver.find_element(By.XPATH, '/html/body/div/main/section/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/button[2]')
btn3.click()
driver.implicitly_wait(5000)

# 파일 업로드 input 요소 찾기
file_path = os.path.abspath("students_data.xlsx")  # 업로드할 파일의 절대 경로
driver.find_element(By.CSS_SELECTOR, "input[type='file']").send_keys(file_path)
driver.implicitly_wait(5000)

# 파일 등록 버튼
btn5 = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/section/div[3]/button')
btn5.click()
driver.implicitly_wait(5000)
# 이후 작업 수행 가능

input("종료금지")

# 작업이 끝나면 브라우저 닫기
driver.quit()

