import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# 이 줄이 누락되었거나 아래쪽에 있을 확률이 높습니다!
from state import ResearchState 
from datetime import datetime
load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)
def search_node(state: ResearchState):
    # 실제 오늘 날짜를 가져옵니다.
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    # 쿼리를 훨씬 더 공격적으로 바꿉니다.
    # 'current events', 'breaking news', 'today' 같은 단어를 섞어주세요.
    query = f"healthcare AI and medical data news published strictly on {current_date} or late February 2026"
    
    from tools.search_tool import search_medical_ai_news
    news = search_medical_ai_news.invoke(query)
    
    # 검색된 뉴스 날짜가 진짜 오늘인지 터미널에서 확인하기 위함
    print(f"\n--- [검색된 뉴스 타임라인: {current_date}] ---")
    for n in news:
        print(f"📌 {n['title'][:50]}... | URL: {n['url']}")
        
    return {"raw_news": news}

def analysis_node(state: ResearchState):
    content = str(state['raw_news'])
    # LLM이 딴소리 못하게 '제공된 텍스트'라는 점을 강조합니다.
    prompt = (
        f"당신은 전문 리서치 어시스턴트입니다. 아래 제공된 [검색 결과] 리스트에 실제로 언급된 "
        f"최신 기술 용어나 영문 약어 3개를 찾아 풀이해주세요.\n\n"
        f"**주의: 당신의 사전 지식을 사용하지 말고, 오직 검색 결과에 나온 구체적인 고유명사나 기술 위주로 선택하세요.**\n"
        f"[검색 결과]:\n{content}"
    )
    response = llm.invoke([HumanMessage(content=prompt)])
    return {"term_glossary": {"terms": response.content}}

def summary_node(state: ResearchState):
    content = str(state['raw_news'])
    glossary = state['term_glossary']
    # '오늘 날짜'의 뉴스를 요약하라고 명시합니다.
    prompt = (
        f"당신은 의료 AI 전문 분석가입니다. 아래 [검색 결과]를 바탕으로 '오늘의 가장 중요한 변화'를 요약하세요.\n"
        f"1. 일반적인 이야기가 아닌, 검색 결과에 등장한 구체적인 회사명, 제품명, 혹은 연구 수치를 포함하세요.\n"
        f"2. 출처 URL을 각 항목 끝에 반드시 첨부하세요.\n"
        f"3. 한글로 작성하되 전문 용어는 병기하세요.\n\n"
        f"[검색 결과]:\n{content}\n"
        f"[참고 용어]:\n{glossary}"
    )
    response = llm.invoke([HumanMessage(content=prompt)])
    return {"final_summary": response.content}


def email_delivery_node(state: ResearchState):
    sender = os.getenv("EMAIL_SENDER")
    password = os.getenv("EMAIL_PASSWORD")
    receiver = os.getenv("EMAIL_RECEIVER")

    if not all([sender, password, receiver]):
        print("❌ 이메일 환경 변수가 설정되지 않았습니다.")
        return state

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = f"🏥 의료 AI 리서치 일일 리포트 ({datetime.now().strftime('%Y-%m-%d')})"

    # HTML 형식으로 본문 꾸미기
    html_content = f"""
    <html>
      <body style="font-family: Arial, sans-serif; line-height: 1.6;">
        <h2 style="color: #2c3e50;">오늘의 의료 AI 뉴스 요약</h2>
        <hr>
        <h3 style="color: #2980b9;">🔍 전문 용어 풀이</h3>
        <div style="background-color: #f4f7f6; padding: 15px; border-radius: 5px;">
            {state['term_glossary'].get('terms', '').replace('\n', '<br>')}
        </div>
        
        <h3 style="color: #2980b9;">📝 핵심 요약 및 인사이트</h3>
        <div style="padding: 10px;">
            {state['final_summary'].replace('\n', '<br>')}
        </div>
        <br>
        <p style="font-size: 0.8em; color: #95a5a6; border-top: 1px solid #eee; pt: 10px;">
            본 리포트는 혜진님의 AI 에이전트에 의해 자동 생성되었습니다.
        </p>
      </body>
    </html>
    """
    msg.attach(MIMEText(html_content, 'html'))

    try:
        # Gmail SMTP 서버 사용
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender, password)
            server.send_message(msg)
        print("📧 이메일 리포트 전송 성공!")
    except Exception as e:
        print(f"❌ 이메일 전송 실패: {e}")

    return state