from agents.research_agent import run_research
from agents.writer_agent import create_writer_agent
from agents.reviewer_agent import create_reviewer_agent
from memory.memory_manager import MemoryManager

def run_multi_agent_pipeline(user_query: str):
    
    print("\n" + "="*60)
    print("🚀 MULTI-AGENT PIPELINE STARTED")
    print("="*60)
    print(f"📋 Task: {user_query}")
    
    memory = MemoryManager()
    
    print("\n🧠 Checking memory for similar past results...")
    cached = memory.search(user_query)
    
    if cached:
        print("⚡ Found in memory — skipping agents!")
        print("\n" + "="*60)
        print("📊 RESULT FROM MEMORY:")
        print("="*60)
        print(cached)
        return cached
    
    print("🔍 Nothing in memory — running agents...")
    
    # ── AGENT 1: RESEARCHER ──────────────────────────
    print("\n🔍 [AGENT 1] Research Agent working...")
    print("-"*40)
    research_data = run_research(user_query)
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
    
    # ── SAVE TO MEMORY ───────────────────────────────
    print("\n💾 Saving result to memory...")
    memory.save(user_query, final_output)
    
    print("\n" + "="*60)
    print("📊 FINAL OUTPUT FROM MULTI-AGENT SYSTEM:")
    print("="*60)
    print(final_output)
    print("="*60)
    
    return final_output