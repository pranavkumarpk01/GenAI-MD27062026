# AI Travel Agent

A LangChain agent (Gemini) that plans trips using real APIs, with persistent
memory and a Streamlit chat UI.

## What it does

- **Weather** — real current weather via Open-Meteo (free, no API key).
- **Flights / Hotels / general search** — live web results via [Tavily](https://tavily.com).
- **Memory** — chat history saved to a local SQLite file (`chat_memory.db`), so it survives restarts.
- **UI** — a simple Streamlit chat interface, plus the original CLI still works.

## 1. Setup

```bash
cd "AI agent"
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 2. API keys

Edit `.env` and fill in:

```
GOOGLE_API_KEY=your_gemini_key      # https://aistudio.google.com/apikey
TAVILY_API_KEY=your_tavily_key      # https://app.tavily.com (free tier available)
```

## 3. Run it

**Streamlit UI (recommended):**
```bash
streamlit run streamlit_app.py
```
Opens at http://localhost:8501

**CLI (original):**
```bash
python app.py
```
Type `exit` to quit.

## Project structure

```
AI agent/
├── app.py                 # CLI entry point
├── streamlit_app.py        # Web chat UI
├── agent/travel_agent.py   # Agent + tools + memory wiring
├── tools/
│   ├── weater_tool.py       # Real weather (Open-Meteo)
│   ├── flight_tool.py       # Real flight search (Tavily)
│   ├── hotel_tool.py        # Real hotel search (Tavily)
│   └── search_tool.py       # General web search (Tavily)
├── memory/memory.py         # SQLite-backed chat history
├── prompts/system_prompt.py # System prompt
└── utils/llm.py             # Gemini LLM setup
```

## How memory works

Each user gets a `session_id` (the CLI uses `"cli-user"`, Streamlit uses
`"streamlit-user"`). All messages for that session are stored in
`chat_memory.db` (SQLite), so the agent remembers past conversation even
after you close and reopen the app. To start fresh, delete `chat_memory.db`
or use the "Clear chat" button in the sidebar.

## Notes

- Flights/hotels use live web search (Tavily) rather than a real booking
  API, since most airline/hotel APIs require paid partner access — this
  keeps setup simple while still giving real, current results.
- `chat_memory.db` and `.env` are gitignored so your keys and chat history
  never get committed.
