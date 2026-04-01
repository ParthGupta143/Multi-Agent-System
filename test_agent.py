from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Load API key
load_dotenv()

# LLaMA 3.3 70B — completely free!
llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)

# Test it!
response = llm.invoke("What is a Multi-Agent System? Explain in 3 lines.")

print(response.content)