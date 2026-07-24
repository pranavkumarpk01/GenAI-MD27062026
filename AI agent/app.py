from agent.travel_agent import executor

while True:
    query = input("\nYou :")
    

    response = executor.invoke(
       {
           "input":query
       }
    )
    print("\nAgent:\n")
    print(response["output"])