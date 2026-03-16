# 1. 베이스 이미지 설정 (파이썬 3.12 슬림 버전 사용)
FROM python:3.12-slim

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. 필요한 파일 복사 (라이브러리 목록)
COPY requirements.txt .

# 4. 라이브러리 설치
RUN pip install --no-cache-dir -r requirements.txt

# 5. 소스 코드 및 .env 파일 전체 복사
COPY . .

# 6. FastAPI 서버 실행 (8000 포트)
EXPOSE 8000

# 7. 서버 실행 명령
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]