from typing import TypedDict, List, Annotated
import operator

class ResearchState(TypedDict):
    topic: str                      # 검색 주제 (의료 데이터, AI 뉴스 등)
    raw_news: Annotated[List[dict], operator.add]  # 검색된 뉴스 리스트 (데이터를 계속 합침)
    term_glossary: dict             # 의료/AI 전문 용어 풀이
    final_summary: str              # 최종 요약 리포트