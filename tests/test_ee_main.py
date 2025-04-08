# ee_main이 제대로 작동하는지 확인하기 위한 테스트

import sys
from unittest.mock import patch, MagicMock

sys.modules["crawling.crawling_main"] = MagicMock()

from EE.main import ee_today_notices

@patch("EE.main.filter_date_notices")
@patch("EE.main.crawling_notices")
def test_ee_today_notices_filters_today(mock_crawling, mock_filter):
    mock_crawling.return_value = [
        {"title": "EE 공지", "date": "2025.04.08", "link": "https://example.com"}
    ]
    mock_filter.return_value = [mock_crawling.return_value[0]]

    result = ee_today_notices()

    assert isinstance(result, list)
    assert result[0]["title"] == "EE 공지"
