### 컴퓨터공학과 - 대학원공지
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from fake_useragent import UserAgent
import time

from dotenv import load_dotenv

from crawl_notices import crawl_today_notices

#################### Detecting Site에 따른 변경부 ####################
detecting_website = (
    "https://scc.sogang.ac.kr/front/cmsboardlist.do?siteId=cs&bbsConfigFK=1747"
)
detecting_interval = 60
notice_num = 20 #10개 + 공지 개수인데.. 공지 개수 어케 알아옴?

xpath_list = []
for i in range(1, notice_num):
    notice = {
        "title": f"/html/body/div/div[4]/div[2]/div[4]/div/div/ul/li[{i}]/div/div[2]/a",
        "registered_date": f"/html/body/div/div[4]/div[2]/div[4]/div/div/ul/li[{i}]/div/div[2]/div/span[2]"
    }
    xpath_list.append(notice)
#################### Detecting Site에 따른 변경부 ###################


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

crawl_today_notices(driver, xpath_list)