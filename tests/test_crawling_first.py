# crawling_notices() 함수가 Selenium 객체들을 사용해 공지 정보를 추출하는 로직이 잘 작동하는지 mock 기반 검증 (외부 사이트 X)
from unittest.mock import patch, MagicMock
from crawling.crawling_first import crawling_notices

@patch("crawling.crawling_first.webdriver.Chrome")
@patch("crawling.crawling_first.counting_notices", return_value=2)
@patch("crawling.crawling_first.making_xpath_list")
def test_crawling_notices(mock_xpath_list, mock_count, mock_driver):
    # 드라이버 & 요소들 목 객체 생성
    mock_driver_instance = MagicMock()
    mock_driver.return_value = mock_driver_instance

    # XPath 리스트 반환
    mock_xpath_list.return_value = [
        {
            "title": "/html/title",
            "registered_date": "/html/date"
        }
    ]

    # 날짜 요소 mock
    el_date = MagicMock()
    el_date.text = "2025.04.08"

    # 제목 요소 mock
    el_title = MagicMock()
    el_title.text = "공지 제목"
    el_title.get_attribute.return_value = "https://example.com"

    # find_element가 특정 XPath로 불렸을 때 반환할 객체 지정
    def find_element_mock(by, value):
        if value == "/html/date":
            return el_date
        elif value == "/html/title":
            return el_title
        elif value == "/ul":
            # 공지 리스트 부모 박스 mock
            el_box = MagicMock()
            el_box.find_elements.return_value = [MagicMock(), MagicMock()]  # dummy li 2개
            return el_box
        else:
            return MagicMock()

    mock_driver_instance.find_element.side_effect = find_element_mock

    result = crawling_notices("http://example.com", "/ul", "li", "/a", "/span")

    assert result == [{
        "title": "공지 제목",
        "date": "2025.04.08",
        "link": "https://example.com"
    }]
