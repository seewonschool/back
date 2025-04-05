### 인공지능학과 - 주요공지
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from fake_useragent import UserAgent
import datetime
import time

from dotenv import load_dotenv

from cse.crawl_notices import crawl_today_notices

def AIE_important():
    detecting_website = (
        "https://ai.sogang.ac.kr/front/cmsboardlist.do?siteId=ai&bbsConfigFK=5110"
    )
    detecting_interval = 60

    title_parent = f"/html/body/div/div[4]/div[2]/div[4]/div/div/ul"


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

    # 3초 기다림

    driver.implicitly_wait(10)
    driver.get(detecting_website)
    time.sleep(5)

    el_notice_box = driver.find_element(By.XPATH, title_parent)
    list_items = el_notice_box.find_elements(By.TAG_NAME, "li")
    notice_num = len(list_items)

    xpath_list = []
    for i in range(1, notice_num):
        notice = {
            "title": f"/html/body/div/div[4]/div[2]/div[4]/div/div/ul/li[{i}]/div/div[2]/a",
            "registered_date": f"/html/body/div/div[4]/div[2]/div[4]/div/div/ul/li[{i}]/div/div[2]/div/span[2]"
        }
        xpath_list.append(notice)

    data = crawl_today_notices(driver, xpath_list)
    print(data)
    return data


# old_notices = new_notices.copy()

# try:
#     # slack_api.notify_started(slack_channel)

#     # 반복 실행
#     while True:
#         # 오늘 올라온 공지 detect
#         crawl_today_notices()

#         # 기존 공지-새 공지 비교
#         detect_changed_notices()

#         # 저장하고 있던 공지 업데이트
#         old_notices = new_notices.copy()

#         # 1분 후 다시 실행
#         time.sleep(detecting_interval)
#         driver.refresh()

# finally:
#     driver.quit()
#     # slack_api.notify_terminated(slack_channel)