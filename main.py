# import os
# from dotenv import load_dotenv
# from nodes import search_node, analysis_node, summary_node, email_delivery_node
# # 1. 환경 변수를 가장 먼저 로드합니다.
# load_dotenv()

# from langgraph.graph import StateGraph, START, END
# # 우리가 만든 파일들에서 필요한 클래스와 함수를 가져옵니다.
# from state import ResearchState
# from nodes import search_node, analysis_node, summary_node

# # 2. 그래프 빌더 초기화 (우리가 정의한 ResearchState 구조를 따름)
# builder = StateGraph(ResearchState)

# # 3. 노드 추가 (각 노드의 이름과 연결될 함수 매핑)
# builder.add_node("search_news", search_node)
# builder.add_node("analyze_terms", analysis_node)
# builder.add_node("summarize", summary_node)
# builder.add_node("deliver_email", email_delivery_node) # 슬랙 대신 이메일 노드 사용
# # 4. 흐름(Edge) 정의
# # 시작 -> 뉴스 검색 -> 용어 분석 -> 요약 -> 종료
# builder.add_edge(START, "search_news")
# builder.add_edge("search_news", "analyze_terms")
# builder.add_edge("analyze_terms", "summarize")
# builder.add_edge("summarize", "deliver_email") # 요약 후 바로 이메일 전송
# builder.add_edge("deliver_email", END)
# # 5. 그래프 컴파일
# graph = builder.compile()

# # 6. 실행 로직
# if __name__ == "__main__":
#     print("🚀 의료 AI 리서치 에이전트를 시작합니다...")
    
#     # 에이전트에게 줄 첫 번째 질문(주제)
#     initial_input = {
#         "topic": "의료 데이터 활용과 생성형 AI 기술 트렌드",
#         "raw_news": [], # Annotated[list, operator.add]이므로 빈 리스트로 초기화
#         "term_glossary": {},
#         "final_summary": ""
#     }
    
#     # 그래프 실행
#     try:
#         result = graph.invoke(initial_input)
        
#         print("\n" + "="*60)
#         print("🔍 [전문 용어 풀이]")
#         print(result.get('term_glossary', {}).get('terms', '분석된 용어가 없습니다.'))
        
#         print("\n📝 [오늘의 의료 AI 뉴스 요약]")
#         print(result.get('final_summary', '요약된 내용이 없습니다.'))
#         print("="*60 + "\n")
        
#     except Exception as e:
#         print(f"❌ 실행 중 오류가 발생했습니다: {e}")



# 260316
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

# 기존에 만드신 노드와 상태 구조 가져오기
from nodes import search_node, analysis_node, summary_node, email_delivery_node
from state import ResearchState
from langgraph.graph import StateGraph, START, END

# 1. 환경 변수 로드
load_dotenv()

# 2. LangGraph 워크플로우 정의 (기존 로직 유지)
builder = StateGraph(ResearchState)
builder.add_node("search_news", search_node)
builder.add_node("analyze_terms", analysis_node)
builder.add_node("summarize", summary_node)
builder.add_node("deliver_email", email_delivery_node)

builder.add_edge(START, "search_news")
builder.add_edge("search_news", "analyze_terms")
builder.add_edge("analyze_terms", "summarize")
builder.add_edge("summarize", "deliver_email")
builder.add_edge("deliver_email", END)

# 그래프 컴파일
graph = builder.compile()

# 3. FastAPI 앱 초기화
app = FastAPI(
    title="Medical AI Insight Agent API",
    description="뉴스 검색부터 요약, 이메일 발송까지 수행하는 AI 에이전트 서비스"
)

# 입력 데이터 형식 정의
class AgentRequest(BaseModel):
    topic: str = "의료 데이터 활용과 생성형 AI 기술 트렌드"

# 4. API 엔드포인트 정의
@app.get("/")
def read_root():
    return {"message": "Medical AI Agent API is running!"}

@app.post("/run-agent")
async def run_agent(request: AgentRequest):
    """
    에이전트를 실행하고 최종 요약 결과를 반환합니다.
    동시에 설정된 수신자에게 이메일을 발송합니다.
    """
    initial_input = {
        "topic": request.topic,
        "raw_news": [],
        "term_glossary": {},
        "final_summary": ""
    }
    
    try:
        # 에이전트 실행
        result = graph.invoke(initial_input)
        
        return {
            "status": "success",
            "topic": request.topic,
            "analysis": result.get('term_glossary', {}).get('terms'),
            "summary": result.get('final_summary'),
            "message": "리포트 생성 및 이메일 발송이 완료되었습니다."
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 5. 로컬 테스트용 실행 설정
if __name__ == "__main__":
    import uvicorn
    print("🚀 서버를 시작합니다. http://127.0.0.1:8000/docs 에서 테스트하세요.")
    uvicorn.run(app, host="127.0.0.1", port=8000)