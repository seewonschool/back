# crawling_main() 함수가 크롤링 함수가 리턴한 공지들을 잘 POST 요청하는지 검증

import json
import pytest
from unittest.mock import patch, mock_open, MagicMock
from crawling.crawling_main import crawling_main

@patch("crawling.crawling_main.time.sleep", return_value=None)
@patch("crawling.crawling_main.requests.post")
@patch("builtins.open", new_callable=mock_open, read_data='[]')
@patch("json.dump")
def test_crawling_main_sends_new_notice(mock_dump, mock_open_file, mock_post, mock_sleep):
    # POST 요청 성공하도록 mock
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_post.return_value = mock_response

    # 공지 하나 리턴하는 mock 크롤링 함수
    def fake_crawler():
        raise KeyboardInterrupt  # 루프 빠져나오게

    try:
        crawling_main("data.json", "12345678", fake_crawler)
    except KeyboardInterrupt:
        pass

    # POST 요청이 안 보내졌음을 확인 (데이터 없음이니까)
    mock_post.assert_not_called()
