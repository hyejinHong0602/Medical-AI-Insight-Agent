# 1. 훨씬 가벼운 slim 버전 사용 (약 150MB 내외)
FROM python:3.12-slim

WORKDIR /app

# 2. 캐시 파일을 남기지 않도록 설치 옵션 조정
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]