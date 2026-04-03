from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import time
from orchestrator import run_multi_agent_pipeline

# FastAPI app initialize
app = FastAPI(
    title="Multi-Agent Task Automation API",
    description="AI-powered pipeline with Research, Writer & Reviewer agents",
    version="1.0.0"
)

# CORS — React frontend ke liye zaruri hai
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── REQUEST/RESPONSE MODELS ──────────────────────────
class PipelineRequest(BaseModel):
    query: str

class PipelineResponse(BaseModel):
    status: str
    query: str
    output: str
    time_taken: float

# ── ROUTES ───────────────────────────────────────────

@app.get("/")
def home():
    return {
        "message": "Multi-Agent System API is running! 🤖",
        "endpoints": {
            "POST /run-pipeline": "Run the full agent pipeline",
            "GET /health": "Check API health",
            "GET /docs": "API documentation"
        }
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy ✅",
        "agents": ["Research Agent", "Writer Agent", "Reviewer Agent"],
        "memory": "ChromaDB Active"
    }

@app.post("/run-pipeline", response_model=PipelineResponse)
def run_pipeline(request: PipelineRequest):
    
    if not request.query.strip():
        raise HTTPException(
            status_code=400,
            detail="Query cannot be empty!"
        )
    
    if len(request.query) > 500:
        raise HTTPException(
            status_code=400,
            detail="Query too long! Max 500 characters."
        )
    
    try:
        print(f"\n🌐 API Request received: {request.query}")
        
        start_time = time.time()
        output = run_multi_agent_pipeline(request.query)
        end_time = time.time()
        
        time_taken = round(end_time - start_time, 2)
        
        return PipelineResponse(
            status="success",
            query=request.query,
            output=output,
            time_taken=time_taken
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Pipeline error: {str(e)}"
        )