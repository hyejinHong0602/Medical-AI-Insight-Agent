# 🏥 Medical AI Insight Agent
> **LangGraph와 AI 에이전트를 활용한 지능형 의료 IT 뉴스 자동 리서치 시스템**

이 프로젝트는 최신 의료 AI 트렌드를 자동으로 수집하고, 전문 용어를 분석하여 인사이트가 담긴 리포트를 이메일로 발송하는 지능형 에이전트 시스템입니다. 단순한 크롤링을 넘어 **LangGraph의 상태 관리**와 **Multi-Node 워크플로우**를 통해 데이터의 신뢰성과 분석력을 극대화했습니다.

## 🌟 주요 특징 (Key Features)
- **지능형 다단계 워크플로우**: LangGraph를 통한 뉴스 검색 -> 용어 분석 -> 인사이트 도출 -> 결과 전송의 순차적 상태 관리
- **RAG 기반 뉴스 분석**: Tavily Search API를 활용하여 전 세계 의료 IT 뉴스를 실시간 수집 (2026년 최신 데이터 반영 확인)
- **전문 용어 자동 해설**: LLM(Llama 3.3)이 기사 속 어려운 의료/AI 전문 용어를 추출하여 친절하게 풀이
- **완전 자동화 (CI/CD)**: GitHub Actions를 이용해 매일 오전 9시(KST) 자동으로 리포트 생성 및 이메일 발송
- **모듈형 설계**: 검색, 분석, 요약, 전송 로직을 분리하여 유지보수와 확장성(Slack 연동 등) 확보

## 🛠 기술 스택 (Tech Stack)
- **Framework**: LangGraph, LangChain
- **LLM**: Groq (Llama-3.3-70b)
- **Search API**: Tavily Search
- **Embedding**: HuggingFace
- **Automation**: GitHub Actions (CI/CD)
- **Language**: Python 3.12+

## 🏗 시스템 아키텍처 (Workflow)



1. **Search Node**: 지정된 주제에 대한 최신 글로벌 의료 뉴스를 검색
2. **Analysis Node**: 뉴스 본문에서 고유 명사 및 전문 용어(RPM, VBC, EHR 등)를 분석 및 해설
3. **Summary Node**: 분석된 데이터를 바탕으로 비즈니스 인사이트가 포함된 3줄 요약 생성
4. **Email Delivery Node**: HTML 형식의 전문 리포트를 사용자 이메일로 자동 전송

## 🚀 시작하기 (Quick Start)

1. **환경 변수 설정 (.env)**
   ```env
   GROQ_API_KEY=your_key
   TAVILY_API_KEY=your_key
   EMAIL_SENDER=your_gmail
   EMAIL_PASSWORD=your_app_password
   EMAIL_RECEIVER=receiver_email

## 📈 활용 사례 (Use Case)
- 의료 도메인 종사자의 일일 산업 트렌드 모니터링
- AI 기술 도입을 고민하는 의료 기관의 벤치마킹 자료 수집
- 반복적인 리서치 업무의 자동화를 통한 업무 효율성 증대

## 📝 결과물
<img width="1627" height="604" alt="image" src="https://github.com/user-attachments/assets/a207af16-b646-4d76-a3e6-0fe93a91f51e" />

