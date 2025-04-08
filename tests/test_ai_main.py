# AI_main이 제대로 작동하는지 확인하기 위한 테스트

import sys
from unittest.mock import MagicMock, patch

# crawling_main이 실행되지 않도록 아예 가짜로 등록해버리기
sys.modules["crawling.crawling_main"] = MagicMock()

# 이제 AI.main import해도 crawling_main이 실행되지 않음
from AI.main import ai_today_notices

@patch("AI.main.filter_date_notices")
@patch("AI.main.crawling_notices")
def test_ai_today_notices_filters_today(mock_crawling, mock_filter):
    mock_crawling.return_value = [
        {"title": "공지 제목", "date": "2025.04.08", "link": "https://example.com"}
    ]
    mock_filter.return_value = [mock_crawling.return_value[0]]

    result = ai_today_notices()

    assert isinstance(result, list)
    assert result[0]["title"] == "공지 제목"
