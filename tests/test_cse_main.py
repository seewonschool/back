# cse_main이 제대로 작동하는지 확인하기 위한 테스트

import sys
from unittest.mock import patch, MagicMock
from cse.main import cse_today_notices, Notice_Type

# crawling_main 무력화
sys.modules["crawling.crawling_main"] = MagicMock()

@patch("cse.main.filter_date_notices")
@patch("cse.main.crawling_notices")
def test_cse_today_notices_filters_today(mock_crawling, mock_filter):
    mock_crawling.return_value = [
        {"title": "CSE 공지", "date": "2025.04.08", "link": "https://example.com"}
    ]
    mock_filter.return_value = [mock_crawling.return_value[0]]

    result = cse_today_notices(Notice_Type.job)

    assert isinstance(result, list)
    assert result[0]["title"] == "CSE 공지"
