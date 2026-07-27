from langchain_community.chat_message_histories import SQLChatMessageHistory

DB_PATH = "sqlite:///chat_memory.db"


def get_session_history(session_id: str) -> SQLChatMessageHistory:
    """Every session_id gets its own persistent chat history, stored in SQLite."""
    return SQLChatMessageHistory(session_id=session_id, connection=DB_PATH)
