# AIE_main이 제대로 작동하는지 확인하기 위한 테스트

import sys
from unittest.mock import patch, MagicMock

# crawling_main 무력화
sys.modules["crawling.crawling_main"] = MagicMock()

from AIE.main import aie_today_notices

@patch("AIE.main.filter_date_notices")
@patch("AIE.main.crawling_notices")
def test_aie_today_notices_filters_today(mock_crawling, mock_filter):
    mock_crawling.return_value = [
        {"title": "AIE 공지", "date": "2025.04.08", "link": "https://example.com"}
    ]
    mock_filter.return_value = [mock_crawling.return_value[0]]

    result = aie_today_notices()

    assert isinstance(result, list)
    assert result[0]["title"] == "AIE 공지"
