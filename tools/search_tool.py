import os
from tavily import TavilyClient
from langchain_core.tools import tool

@tool
def search_medical_ai_news(query: str) -> list:
    """최신 의료 및 AI 관련 뉴스를 검색합니다."""
    tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
    # search_depth="advanced"로 설정하면 더 깊은 내용을 가져옵니다.
    response = tavily.search(
        query=query, 
        search_depth="advanced", 
        max_results=5,
        include_domains=["medgadget.com", "healthcareitnews.com", "mobihealthnews.com"], # 신뢰할 수 있는 뉴스 사이트 한정
        days=7 # 이 부분이 핵심입니다!
    )
    return response['results']