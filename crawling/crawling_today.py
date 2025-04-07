# 특정 date에 등록된 notice만 필터링해주는 함수
def filter_date_notices(notices, date):
  filtered_list = []

  for notice in notices:
    if notice["date"] == date:
      filtered_list.append(notice)
  
  return filtered_list