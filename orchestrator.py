from agents.research_agent import create_research_agent
from agents.writer_agent import create_writer_agent
from agents.reviewer_agent import create_reviewer_agent

def run_multi_agent_pipeline(user_query: str):
    
    print("\n" + "="*60)
    print("🚀 MULTI-AGENT PIPELINE STARTED")
    print("="*60)
    print(f"📋 Task: {user_query}")
    
    # ── AGENT 1: RESEARCHER ──────────────────────────
    print("\n🔍 [AGENT 1] Research Agent working...")
    print("-"*40)
    
    researcher = create_research_agent()
    research_result = researcher.invoke({"input": user_query})
    research_data = research_result["output"]
    
    print("✅ Research Complete!")
    
    # ── AGENT 2: WRITER ──────────────────────────────
    print("\n✍️  [AGENT 2] Writer Agent working...")
    print("-"*40)
    
    writer = create_writer_agent()
    report = writer.invoke({"research_data": research_data})
    
    print("✅ Report Written!")
    
    # ── AGENT 3: REVIEWER ────────────────────────────
    print("\n🔎 [AGENT 3] Reviewer Agent working...")
    print("-"*40)
    
    reviewer = create_reviewer_agent()
    final_output = reviewer.invoke({"report": report})
    
    print("✅ Review Complete!")
    
    # ── FINAL OUTPUT ─────────────────────────────────
    print("\n" + "="*60)
    print("📊 FINAL OUTPUT FROM MULTI-AGENT SYSTEM:")
    print("="*60)
    print(final_output)
    print("="*60)
    
    return final_output