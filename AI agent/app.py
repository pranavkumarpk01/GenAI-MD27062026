from agent.travel_agent import executor
from utils.format import extract_output_text

SESSION_ID = "cli-user"

print("Travel Agent ready. Type 'exit' to quit.")

while True:
    query = input("\nYou: ")
    if query.strip().lower() in ("exit", "quit"):
        break

    response = executor.invoke(
        {"input": query},
        config={"configurable": {"session_id": SESSION_ID}},
    )
    print("\nAgent:\n")
    print(extract_output_text(response["output"]))
