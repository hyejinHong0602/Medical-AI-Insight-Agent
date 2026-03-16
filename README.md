# 🏥 Medical AI Insight Agent
> **LangGraph와 Docker/AWS를 활용한 지능형 의료 IT 뉴스 자동 리서치 및 서빙 시스템**

이 프로젝트는 최신 의료 AI 트렌드를 자동으로 수집하고, 전문 용어를 분석하여 인사이트가 담긴 리포트를 이메일로 발송하는 지능형 에이전트 시스템입니다. 단순한 로직 구현을 넘어 **FastAPI를 통한 서빙**, **Docker 이미지 생성**, 그리고 **AWS EC2 배포**를 통해 실제 운영 가능한 수준의 아키텍처를 구축했습니다.

---

## 🚀 Live Demo 
현재 AWS 클라우드에 배포되어 있으며, 아래 링크를 통해 API를 직접 테스트해 보실 수 있습니다.
* **Swagger UI**: [http://52.79.229.89:8000/docs](http://52.79.229.89:8000/docs)
  *(에이전트 실행을 위해 `POST /run` 엔드포인트에서 `Execute`를 클릭해 보세요.)*

---

## 🌟 주요 특징 (Key Features)
- **지능형 다단계 워크플로우**: LangGraph를 통한 뉴스 검색 → 용어 분석 → 인사이트 도출 → 결과 전송의 순차적 상태 관리
- **RESTful API 서빙**: FastAPI를 활용하여 에이전트 실행 로직을 API 엔드포인트로 구현
- **컨테이너 기반 배포 최적화**: Docker 이미지 경량화를 통해 클라우드 배포 효율성 및 속도 극대화
- **RAG 기반 뉴스 분석**: Tavily Search API를 활용하여 2026년 최신 글로벌 의료 IT 뉴스 실시간 수집
- **전문 용어 자동 해설**: LLM(Llama 3.3)이 기사 속 어려운 전문 용어(RPM, VBC, EHR 등)를 추출하여 분석 리포트 제공

## 🏗 시스템 아키텍처 (Architecture)

1. **Search Node**: 지정된 주제에 대한 최신 글로벌 의료 뉴스를 검색
2. **Analysis Node**: 뉴스 본문에서 고유 명사 및 전문 용어를 분석 및 해설
3. **Summary Node**: 분석 데이터를 바탕으로 비즈니스 인사이트가 포함된 3줄 요약 생성
4. **Email Delivery Node**: HTML 형식의 전문 리포트를 사용자 이메일로 자동 전송
5. **Serving Layer**: Docker 컨테이너 내에서 FastAPI 서버가 구동되어 외부 요청 처리

## 🛠 기술 스택 (Tech Stack)
- **Framework**: LangGraph, FastAPI, LangChain
- **LLM**: Groq (Llama-3.3-70b)
- **Infrastructure**: **Docker (Optimized)**, **AWS EC2**, **AWS ECR**
- **Search API**: Tavily Search
- **Language**: Python 3.12+

## 📈 인프라 및 배포 성과 (Infrastructure & Deployment)
안정적인 서비스 운영과 보안을 위해 다음과 같은 배포 환경을 구축했습니다.

* **컨테이너 기반 환경 격리**: Docker를 활용하여 로컬 개발 환경과 AWS 서버 환경의 일관성을 유지하고, 종속성 충돌 없는 안정적인 서빙 환경 구축
* **클라우드 인프라 프로비저닝**: AWS EC2 인스턴스를 활용하여 24/7 가동 가능한 서버 환경을 구축하고, ECR(Elastic Container Registry)을 통한 이미지 관리 자동화
* **보안 최적화 및 환경 분리**:
 1. AWS 보안 그룹(Security Group) 설정을 통해 서비스에 필요한 포트(8000)만 제한적으로 개방
 2. API Key 및 이메일 계정 정보 등 민감 데이터를 소스코드와 분리하여 컨테이너 실행 시 환경 변수(-e)로 주입하는 보안 프로토콜 준수
---

## 💻 시작하기 (How to Run)

### 1. 환경 변수 설정 (.env)
프로젝트 루트 폴더에 `.env` 파일을 생성하고 아래 정보를 입력합니다.
```코드 스니펫
GROQ_API_KEY=your_key
TAVILY_API_KEY=your_key
EMAIL_SENDER=your_gmail
EMAIL_PASSWORD=your_app_password
EMAIL_RECEIVER=receiver_email
```
### 2. Docker를 이용한 즉시 실행
별도의 환경 설정 없이 Docker를 통해 로컬에서 즉시 실행할 수 있습니다.
```Bash
# 이미지 빌드
docker build -t medical-ai-agent .

# 컨테이너 실행
docker run -d -p 8000:8000 --env-file .env --name medical-agent medical-ai-agent
```

## 📝 결과물 예시
에이전트가 생성한 의료 AI 분석 리포트 메일 예시입니다.
<img width="1844" height="533" alt="image" src="https://github.com/user-attachments/assets/de6e96df-b920-4bc6-a887-965ed0fa733b" />
<img width="1471" height="435" alt="image" src="https://github.com/user-attachments/assets/d155a218-2c16-4bdc-b8df-1975d95a09d6" />
<img width="1441" height="475" alt="image" src="https://github.com/user-attachments/assets/40274f94-a47b-4d20-8f89-0c25b8a5d02d" />
<img width="1417" height="473" alt="image" src="https://github.com/user-attachments/assets/304c783f-f47e-4cc6-8c71-67de84d0f07a" />

## 🎯 추후 발전 방향
* 의료 분야를 넘어 경제, 기술 등 다양한 도메인별 뉴스레터 파이프라인 확장
* Slack 및 Discord 연동을 통한 실시간 알림 시스템 구축
