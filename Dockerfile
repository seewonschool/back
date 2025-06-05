# Python 3.11 slim 기반 이미지
FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive

# 시스템 패키지 설치
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    curl \
    unzip \
    wget \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# 작업 디렉토리 설정
WORKDIR /app

# requirements.txt 먼저 복사 및 설치
COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt

# python3가 selenium 설치된 python을 가리키도록 강제 연결
RUN ln -sf /usr/local/bin/python /usr/bin/python3

# 전체 프로젝트 복사
COPY . .

# Chrome 환경변수 설정
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver
ENV PATH=$CHROMEDRIVER_PATH:$PATH

# entrypoint.sh 실행 권한 부여
RUN chmod +x /app/entrypoint.sh

# 엔트리포인트 실행
ENTRYPOINT ["/app/entrypoint.sh"]

