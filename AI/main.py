### AI기반 자유전공학부 - 주요공지
import datetime
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from crawling.crawling_first import crawling_notices
from crawling.crawling_today import filter_date_notices
from crawling.crawling_main import crawling_main
from const.kakao_conversation import KakaoConversaionId

def ai_today_notices():
  notices = crawling_notices("https://aibased.sogang.ac.kr/front/cmsboardlist.do?siteId=aibased&bbsConfigFK=7510", "/html/body/div/div[4]/div[2]/div[3]/div/div/ul", "li", "/div/div[2]/a", "/div/div[2]/div/span[2]")
  
  # UTC+9 Timezone에서의 오늘 날짜 formatting
  date_today = (datetime.datetime.utcnow() + datetime.timedelta(hours=9)).strftime("%Y.%m.%d")

  return filter_date_notices(notices, date_today)

crawling_main('data.json', KakaoConversaionId.AI, ai_today_notices)