# Python 3.11 이미지 사용
FROM python:3.11-slim

# 작업 디렉토리 설정
WORKDIR /ai/project/back/AI

# 시스템 의존성 설치 (크롬, 크롬 드라이버, 기타 필수 패키지)
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    chromium \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 크롬 드라이버 설치 (webdriver-manager 사용)
RUN pip install --no-cache-dir webdriver-manager

# 전체 프로젝트 파일 복사 (루트에서 Docker 빌드를 할 때)
COPY . .

# Python 의존성 설치
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 환경 변수 로딩
RUN pip install python-dotenv

# 애플리케이션 실행 (main.py 실