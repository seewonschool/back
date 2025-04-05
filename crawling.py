from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
from dotenv import load_dotenv

import time

from model.major import Major

# 한 페이지에 게시된 공지 개수를 찾아주는 함수
def counting_notices(driver, parent_path, child_tagname):
  el_notice_box = driver.find_element(By.XPATH, parent_path)
  list_items = el_notice_box.find_elements(By.TAG_NAME, child_tagname)
  return len(list_items)


# 크롤링 path list 만들어주는 함수
# *_path: /로 시작
def making_xpath_list(notice_num, parent_path, child_tagname, title_detail_path, date_detail_path):
  xpath_list = []

  for i in range(1, notice_num):
      notice = {
          "title": f"{parent_path}/{child_tagname}[{i}]{title_detail_path}",
          "registered_date": f"{parent_path}/{child_tagname}[{i}]{date_detail_path}"
      }
      xpath_list.append(notice)
  
  return xpath_list


# 첫 페이지를 크롤링해오는 로직
def crawling_notices(website_link, notice_parent_path, notice_child_tagname, title_detail_path, date_detail_path):

  load_dotenv()

  # Selenium options
  chrome_options = webdriver.ChromeOptions()
  ua = UserAgent()
  userAgent = ua.random
  chrome_options.add_argument("--headless")
  chrome_options.add_argument("--no-sandbox")
  chrome_options.add_argument("--disable-dev-shm-usage")
  chrome_options.add_argument(f"user-agent={userAgent}")

  # 드라이버 실행
  driver = webdriver.Chrome(
      service=Service(ChromeDriverManager().install()), 
      options=chrome_options
  )

  # 웹페이지 로딩
  driver.implicitly_wait(10)
  driver.get(website_link)
  time.sleep(5)

  notice_num = counting_notices(driver, notice_parent_path, notice_child_tagname)

  xpath_list = making_xpath_list(notice_num, notice_parent_path, notice_child_tagname, title_detail_path, date_detail_path)

  notice_list = []
  for each_xpath in xpath_list:
    notice_date = driver.find_element(By.XPATH, each_xpath["registered_date"]).text
    el_notice_title = driver.find_element(By.XPATH, each_xpath["title"])

    notice_title = el_notice_title.text
    notice_href = el_notice_title.get_attribute("href")
    notice_list.append(dict(
        title = notice_title, 
        date = notice_date, 
        link = notice_href
    ))

  driver.quit()
  
  return notice_list