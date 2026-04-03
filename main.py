from orchestrator import run_multi_agent_pipeline

print("🔥 RUN 1 — Fresh query (agents will run)")
run_multi_agent_pipeline(
    "Explain Multi-Agent Systems and their real world applications"
)

print("\n\n" + "🔥"*20)
print("🔥 RUN 2 — Same query (memory will respond!)")
run_multi_agent_pipeline(
    "Explain Multi-Agent Systems and their real world applications"
)