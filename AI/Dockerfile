# Python 3.11 slim 이미지 사용
FROM python:3.11-slim

# 비대화 모드 설정
ENV DEBIAN_FRONTEND=noninteractive

# 시스템 의존성 설치
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    curl \
    unzip \
    wget \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# 작업 디렉토리 설정
WORKDIR /app/AI

# AI 디렉토리 복사
COPY AI/ /app/AI

# 외부 모듈들 루트 기준으로 복사
COPY crawling /app/crawling
COPY const /app/const
COPY model /app/model

# AI/ 디렉토리 내 data.json 파일 복사
COPY AI/data.json /app/AI/data.json

# Chrome 환경 변수
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver
ENV PATH=$CHROMEDRIVER_PATH:$PATH

# Python 디펜던시 설치
COPY AI/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 실행
CMD ["python", "main.py"]
