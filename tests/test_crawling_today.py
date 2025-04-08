# filter_date_notices() 함수가 특정 날짜에 등록된 공지들만 필터링하는 로직이 잘 작동하는지 검증

from crawling.crawling_today import filter_date_notices

def test_filter_date_notices_returns_today_only():
    notices = [
        {"title": "공지1", "date": "2025.04.08"},
        {"title": "공지2", "date": "2025.04.07"},
    ]

    result = filter_date_notices(notices, "2025.04.08")

    assert len(result) == 1
    assert result[0]["title"] == "공지1"
