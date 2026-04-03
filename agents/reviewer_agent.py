from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

def create_reviewer_agent():
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.3)
    
    prompt = PromptTemplate.from_template("""
You are a strict Quality Reviewer Agent.

Your job is to review a report and improve it.

Original Report:
{report}

Review it for:
1. Clarity — is it easy to understand?
2. Completeness — is anything missing?
3. Accuracy — does it make sense?
4. Structure — is it well organized?

Then provide:
- REVIEW SCORE: X/10
- IMPROVEMENTS MADE: (list what you changed)
- FINAL IMPROVED REPORT: (the improved version)
""")
    
    chain = prompt | llm | StrOutputParser()
    
    return chain