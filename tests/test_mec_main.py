# mec_main이 제대로 작동하는지 확인하기 위한 테스트

import sys
from unittest.mock import patch, MagicMock

# crawling_main 실행 방지
sys.modules["crawling.crawling_main"] = MagicMock()

from mec.main import mec_today_notices  # ✅ 함수명 정확하게

@patch("mec.main.filter_date_notices")
@patch("mec.main.crawling_notices")
def test_mec_today_notices_filters_today(mock_crawling, mock_filter):
    mock_crawling.return_value = [
        {"title": "MEC 공지", "date": "2025.04.08", "link": "https://example.com"}
    ]
    mock_filter.return_value = [mock_crawling.return_value[0]]

    result = mec_today_notices()

    assert isinstance(result, list)
    assert result[0]["title"] == "MEC 공지"
