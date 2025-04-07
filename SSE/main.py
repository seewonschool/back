### 시스템반도체공학과과 - 주요공지

import datetime
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from crawling.crawling_first import crawling_notices
from crawling.crawling_today import filter_date_notices
from crawling.crawling_main import crawling_main
from const.kakao_conversation import KakaoConversaionId

def sse_today_notices():
  notices = crawling_notices("https://sse.sogang.ac.kr/kor/community/notice.php", "/html/body/div[2]/div[2]/div/div/div/div/div[2]/div[2]/table/tbody", "tr", "/td[2]/div/a", "/td[3]")
  
  # UTC+9 Timezone에서의 오늘 날짜 formatting
  date_today = (datetime.datetime.utcnow() + datetime.timedelta(hours=9)).strftime("%Y.%m.%d")

  return filter_date_notices(notices, date_today)

crawling_main('data.json', KakaoConversaionId.SSE, sse_today_notices)