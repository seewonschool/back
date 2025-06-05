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
# 왜 이럴까? 이거 안되나 ㅎ?;; 터미널 봤어? 웅웅 json이 없으시대 엉엉 드렁슨 언니 돌려조..........넵!르겟어 돌리고 돌리이고 언제까지 돌리냐 두근 클 없대 슈발 
current_directory = os.getcwd()
print(f"Current directory: {current_directory}")
crawling_main("./AI/data_ai.json", KakaoConversaionId.AI, ai_today_notices)
# print(f"Absolute path: {os.path.abspath('data_ai.json')}")
# print(f"Current directory: {current_directory}")