from langchain_classic.memory import ConversationBufferMemory

memory = ConversationBufferMemory(
    memory_key ="chat_history",
    return_messages=True
)


#user: I want to go to goa
#AI : Okay.

#Next: Book hotel
#AI" which city