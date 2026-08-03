from app.agents.research_agent import ResearchAgent


agent = ResearchAgent()

response = agent.answer(
    "What is HAC?",
    document_id=7,
    top_k=5
)

print("\n===== PROJECT HELIX RESPONSE =====\n")
print(response)