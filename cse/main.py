from enum import Enum
from .important import cse_important

class Notice_Type(str, Enum):
  important: 1
  general: 2
  graduate: 3
  under: 4
  job: 5

# def cse_today_notices(type: Notice_Type):
#   if(type == 1):
#     notice = cse_important()

  