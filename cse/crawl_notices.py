from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from fake_useragent import UserAgent
import datetime
import time

# 오늘 등록된 공지만 crawl
def crawl_today_notices(driver, xpath_list):
    # new_notices.clear()
    new_list = []
    for each_xpath in xpath_list:
        notice_date = driver.find_element(By.XPATH, each_xpath["registered_date"]).text
        el_notice_title = driver.find_element(By.XPATH, each_xpath["title"])

        notice_title = el_notice_title.text
        notice_href = el_notice_title.get_attribute("href")
        print(notice_title)
        print(notice_date)
        print(notice_href)
        new_list.append(dict(
            title = notice_title, 
            date = notice_date, 
            link = notice_href
        ))
        # if notice_date == date_today:
        #     # notice_title = driver.find_element(By.XPATH, each_xpath["title"])
        #     notice = {
        #         "title": notice_title.text,
        #         "link": notice_title.get_attribute("href"),
        #     }
        #     new_notices.append(notice)

    print(new_list)
    return new_list
  