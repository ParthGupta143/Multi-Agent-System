from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

def create_writer_agent():
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)
    
    prompt = PromptTemplate.from_template("""
You are an expert Technical Writer Agent.

Your job is to take raw research data and convert it into a 
clean, well-structured, professional report.

Raw Research Data:
{research_data}

Write a professional report with these sections:
1. Executive Summary (2-3 lines)
2. Key Findings (bullet points)
3. Real World Applications (3-4 examples)
4. Conclusion (2-3 lines)

Keep it clear, concise and professional.
""")
    
    # Simple chain — no tools needed, just LLM + prompt
    chain = prompt | llm | StrOutputParser()
    
    return chain