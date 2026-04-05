# 🤖 Multi-Agent Task Automation System: OMNI.AI

An AI-powered multi-agent system where specialized agents 
collaborate autonomously to research, write, and review content.

## 🏗️ Architecture
User Input → Research Agent → Writer Agent → Reviewer Agent → Final Output

## 🛠️ Tech Stack
- **LangChain** — Agent framework
- **Groq + LLaMA 3.3 70B** — Free, fast LLM
- **Wikipedia Tool** — Knowledge retrieval
- **Python 3.11** — Core language

## 🤖 Agents
| Agent | Role |
|-------|------|
| Research Agent | Gathers information using tools |
| Writer Agent | Converts research into structured report |
| Reviewer Agent | Reviews, scores & improves the report |

## 🚀 Setup
```bash
git clone https://github.com/ParthGupta143/Multi-Agent-System
cd Multi-Agent-System
python -m venv venv
venv\Scripts\activate
pip install langchain langchain-groq langchain-community python-dotenv wikipedia
```

Add your `GROQ_API_KEY` in `.env` file, then:
```bash
python main.py
```

## 📊 Status
- [x] Phase 1 — Environment Setup  
- [x] Phase 2 — LangChain + Groq Integration
- [x] Phase 3 — Single Research Agent
- [x] Phase 4 — Multi-Agent Pipeline
- [x] Phase 5 — Memory with ChromaDB
- [x] Phase 6 — FastAPI Backend
- [x] Phase 7 — React Frontend Dashboard
- [ ] Phase 8 — Google Cloud Deployment


## 🖥️ UI Screenshot
![Multi-Agent System Dashboard](<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/860c36c5-9810-4c54-ac8b-7a550df1d10a" />
)

## 🚀 Live Demo
- Frontend: localhost:3000
- API Docs: localhost:8000/docs

## 🌐 Live Demo
👉 [OMNI.AI](https://multi-agent-system-iota.vercel.app/)
