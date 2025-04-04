from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from fake_useragent import UserAgent
import datetime
import time

from dotenv import load_dotenv


# 오늘 등록된 공지만 crawl
def crawl_today_notices(driver, xpath_list):
    # new_notices.clear()
    for each_xpath in xpath_list:
        notice_date = driver.find_element(By.XPATH, each_xpath["registered_date"]).text
        notice_title = driver.find_element(By.XPATH, each_xpath["title"]).text
        print(notice_title)
        print(notice_date)
        # if notice_date == date_today:
        #     # notice_title = driver.find_element(By.XPATH, each_xpath["title"])
        #     notice = {
        #         "title": notice_title.text,
        #         "link": notice_title.get_attribute("href"),
        #     }
        #     new_notices.append(notice)