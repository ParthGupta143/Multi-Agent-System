from langchain_groq import ChatGroq
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()

def create_research_agent():
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)

    wiki = WikipediaAPIWrapper(top_k_results=2, doc_content_chars_max=1000)
    search_tool = WikipediaQueryRun(api_wrapper=wiki)
    tools = [search_tool]

    # LangGraph ka create_react_agent — latest way!
    agent = create_react_agent(llm, tools)

    return agent

def run_research(query: str) -> str:
    agent = create_research_agent()
    
    result = agent.invoke({
        "messages": [{"role": "user", "content": f"""
You are an expert Research Agent. 
Research this topic thoroughly and give a detailed summary:
{query}

Use Wikipedia tool to find information. 
Give a comprehensive Final Answer with real world applications.
"""}]
    })
    
    # Last message nikalo
    last_message = result["messages"][-1]
    return last_message.content