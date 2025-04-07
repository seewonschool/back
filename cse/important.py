### 컴퓨터공학과 - 주요공지
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from fake_useragent import UserAgent
import datetime
import time

from dotenv import load_dotenv

old_notices = []
new_notices = []

# UTC+9 Timezone에서의 오늘 날짜 formatting
date_today = (datetime.datetime.utcnow() + datetime.timedelta(hours=9)).strftime(
    "%Y.%m.%d"
)

