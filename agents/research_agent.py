from langchain_groq import ChatGroq
from langchain.agents import AgentExecutor, create_react_agent
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

def create_research_agent():
    # 1. LLM — brain of the agent
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)

    # 2. Tools — what agent CAN do
    wiki = WikipediaAPIWrapper(top_k_results=2, doc_content_chars_max=1000)
    search_tool = WikipediaQueryRun(api_wrapper=wiki)
    tools = [search_tool]

    # 3. Role — who is this agent?
    prompt = PromptTemplate.from_template("""
You are an expert Research Agent. Your job is to research 
any given topic thoroughly and provide a clear, structured summary.

You have access to the following tools:
{tools}

Use this format STRICTLY:
Question: the input question you must answer
Thought: think about what to do
Action: the action to take, must be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (repeat Thought/Action/Observation as needed)
Thought: I now know the final answer
Final Answer: [your detailed research summary here]

Begin!
Question: {input}
Thought: {agent_scratchpad}
""")

    # 4. Create the agent
    agent = create_react_agent(llm, tools, prompt)
    
    # 5. Executor runs the agent loop
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,        # shows agent's thinking process!
        max_iterations=5,    # max 3 search attempts
        handle_parsing_errors=True
    )
    
    return agent_executor