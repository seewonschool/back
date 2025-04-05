import sys
import os

# 현재 스크립트(main.py)의 상위 디렉토리를 sys.path에 추가
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from enum import Enum
from crawling.crawling_first import crawling_notices
from crawling.crawling_today import filter_date_notices

class Notice_Type(str, Enum):
  important = "important"
  general = "general"
  graduate = "graduate"
  under = "under"
  job = "job"

class CSE_Link(str, Enum):
  important = "https://scc.sogang.ac.kr/front/cmsboardlist.do?siteId=cs&bbsConfigFK=1905"
  general = "https://scc.sogang.ac.kr/front/cmsboardlist.do?siteId=cs&bbsConfigFK=1746"
  graduate = "https://scc.sogang.ac.kr/front/cmsboardlist.do?siteId=cs&bbsConfigFK=1747"
  under = "https://scc.sogang.ac.kr/front/cmsboardlist.do?siteId=cs&bbsConfigFK=1745"
  job = "https://scc.sogang.ac.kr/front/cmsboardlist.do?siteId=cs&bbsConfigFK=1748"


def cse_today_notices(type: Notice_Type):
  notices = crawling_notices(CSE_Link[type], "/html/body/div/div[4]/div[2]/div[4]/div/div/ul", "li", "/div/div[2]/a", "/div/div[2]/div/span[2]")
  
  # TODO: 오늘 등록된 것만 거르는 로직 추가
  return filter_date_notices(notices, '2025.03.28')


# print(cse_today_notices(Notice_Type.job))