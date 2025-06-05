from enum import Enum

MajorCode = {
    "컴퓨터공학": "CSE",
    "AI기반 자유전공학부": "AI",
    "인공지능학": "AIE",
    "화공생명공학": "CBE",
    "전자공학": "EE",
    "기계공학": "MEC",
    "시스템반도체공학": "SSE",
}

### 카카오워크 채널 id
class KakaoConversaionId(str, Enum):
  CSE = '12352747' #컴퓨터공학과, 아직 테스트 id
  AI = '12352848' #AI기반 자유전공학부
  AIE = '12352844' #인공지능학과
  CBE = '12352847' #화공생명공학과
  EE = '12352845' #전자공학과
  MEC = '12352843' #기계공학과
  SSE = '12352846' #시스템반도체공학과
