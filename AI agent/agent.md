1.Difference betweeen automation and AI agent is that, an agent contians an LLM , where as automation doesnt contain it..
2.Scenario -> when u want the agent not to do any repettivve task then you would use the concept of memory
3.tools -> It will help your llm and also u r application to get the data from third party applications.

Example flow for a AI agent (book a flight from one place to another)

User -> understand request (LLM) -> search_flights() -> llm(compare the prices , fastest flight) -> book that flight -> send a mail that the flight has been booked to u.

Pranav 22 nd JUly booked a flight banglore to delhi august 10th -> Database











              User
                |

                V

           Prompt

                |

                V

           LLM Brain

                |

      ----------------------

      |     |      |       |

   Memory Tools Planner Reasoner

      |     |      |       |

      --------Environment------

                |

             Observation

                |

          Next Decision


---

# AI Agents — Full Notes (Basics to Advanced)

## 1. What is an AI Agent? (Formal definition)

An **AI agent** is a system built around an LLM that can **perceive** (take in input/context), **reason** (decide what to do), **act** (call tools/APIs to affect the outside world or fetch data), and **observe the result of its own actions**, repeating this loop until it reaches a goal — without a human manually deciding each step.

The key phrase is "LLM as the brain." Everything else — tools, memory, prompts — is scaffolding around that brain so it can actually get things done instead of just talking.

**Real-world definition, in plain terms**: if a plain chatbot is like a very knowledgeable person stuck behind a glass wall (they can only talk to you), an agent is that same person handed a phone, a laptop, and permission to actually make calls, check websites, and take notes — they can now *do* things, not just describe what should be done.

## 2. Agent vs Automation vs Chatbot (the three you'll hear compared constantly)

| | Automation (RPA/scripts) | Chatbot (plain LLM) | AI Agent |
|---|---|---|---|
| Decision-making | Fixed if/else rules, no reasoning | Reasons in language, but can't act | Reasons AND acts |
| Handles unexpected input | Breaks or falls into a default branch | Can respond to it in text | Can adapt its plan and try a different tool |
| Memory | None (stateless steps) | Only within one chat context | Short-term (conversation) and/or long-term (database/vector store) |
| Can touch real systems? | Yes, but only pre-scripted actions | No | Yes, dynamically, based on reasoning |
| Real-world example | A Zapier flow: "when a new email arrives with an attachment, save it to Google Drive" — always the same steps, every time | ChatGPT answering "what's the weather like in Goa in July" from general knowledge (which may be wrong/outdated) | A travel-planning agent that checks live weather, *then* decides whether to recommend Goa, *then* searches real hotel/flight data, adapting its recommendation based on what it finds |

The distinction that matters most: automation follows a script, an agent follows a *goal* and figures out the script itself, tool call by tool call.

## 3. Why do agents need anything beyond "just the LLM"?

Left alone, an LLM has three hard limits:
1. **No real-time or private data** — it can't know today's weather, your company's database, or live flight prices; it was trained on a fixed snapshot of text.
2. **No memory beyond what's pasted into its context window** — close the chat, and everything is gone (unless something outside the LLM stores it).
3. **No ability to act** — it can only produce text. It cannot literally book a flight, send an email, or query a database on its own.

Agents patch all three gaps: **tools** solve (1) and (3), **memory** solves (2). This is the entire reason the agent architecture (LLM + tools + memory + a reasoning loop) exists.

## 4. Anatomy of an agent (expanding your diagram)

```
User → Prompt → LLM (Brain) → [Memory | Tools | Planner | Reasoner] → Environment → Observation → next decision → (loop)
```

**Memory** — where the agent keeps track of what's already happened.
- *Short-term / working memory*: the current conversation only. In this project, `ConversationBufferMemory` — it just keeps the raw back-and-forth so the agent doesn't forget what you said two messages ago.
- *Long-term memory*: persists across sessions, usually backed by a real database or a vector store (for semantic recall — "what did this user ask about last month?"). Not used in this project yet, but this is the direction `memory/memory.py` would grow toward for a production app.
- Real-world example: a customer-support agent that remembers, three days later, that you already tried restarting your router — that's long-term memory backed by a database, not the LLM "remembering" anything itself.

**Tools** — functions or APIs the LLM is allowed to call to get real data or take real actions.
- Real-world examples beyond this project: a calculator tool (LLMs are bad at precise arithmetic), a SQL tool (query a live database), a web-search tool, a "send_email" tool, a "create_calendar_event" tool.
- In this project: `get_weather`, `search_hotels`, `search_flights` — each one is a stand-in for what would be a real weather API, a real hotel-booking API (e.g. Booking.com's API), and a real flight-search API (e.g. Skyscanner/Amadeus) in production.

**Planner** — breaks one big, vague goal into an ordered list of smaller steps.
- Real-world example: "Plan my Goa trip" silently becomes: check weather → search flights → search hotels → compare cost → produce an itinerary. The user never explicitly listed these steps; the agent inferred them.

**Reasoner** — the decision logic that looks at "what do I know so far" and decides "what's the single next best action." In LangChain's tool-calling agents, this *is* the LLM itself, prompted in a loop (see the ReAct pattern below) — there's no separate "reasoner module," it's a role the LLM plays every iteration.

**Environment / Observation** — the real world the tools reach into (an API, a database, a filesystem), and whatever comes back from it. The agent treats tool output as "new information" and folds it back into its next reasoning step.

## 5. The ReAct pattern — the theory behind the loop

Most modern tool-using agents (including this project's `AgentExecutor`) implement a pattern called **ReAct** (Reason + Act): the LLM alternates between *thinking*, *acting* (calling a tool), and *observing* (reading the tool's result), until it decides it has enough information to give a final answer.

A worked trace using this project's actual tools, for the query *"Should I go to Goa, and what are my options?"*:

```
Thought: I should check the weather in Goa before recommending it.
Action: get_weather("Goa")
Observation: "Sunny 31C"

Thought: Good weather. Now let's find hotel options.
Action: search_hotels("Goa")
Observation: ["Taj Resort", "Novotel", "Holiday Inn"]

Thought: Now let's check flights.
Action: search_flights("Goa")
Observation: "Indigo ₹5200"

Thought: I now have weather, hotels, and flights — enough to answer.
Final Answer: Goa has sunny weather (31°C). You could stay at Taj Resort,
Novotel, or Holiday Inn, and fly Indigo for around ₹5200.
```

This is exactly what `verbose=True` on `AgentExecutor` prints to your terminal — you're watching this Thought → Action → Observation cycle happen live. `max_iterations` (default 15) exists to stop this loop from running forever if the LLM never decides it's "done."

## 6. Building blocks in this codebase, explained in depth

### 6.1 Tools (`tools/`)
```python
from langchain.tools import tool

@tool
def get_weather(city: str) -> str:
    """Returns weather information."""
    ...
```
- `@tool` converts a normal Python function into something the LLM can "see" and choose to call.
- The LLM never reads your Python code. It only ever sees: the function **name**, its **docstring** (used as the description of *when/why* to call it), and its **type-hinted arguments** (turned into a JSON schema so the LLM knows what input to provide). This is why a missing docstring throws `ValueError: Function must have a docstring` — without it, the LLM would have zero information about what the tool does.
- Real-world parallel: think of each tool as a one-line job listing — "Returns weather information" is the entire ad the LLM reads before deciding whether this is the right function to call for the user's question.

### 6.2 Prompt template (`prompts/`)
```python
ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    ("placeholder", "{chat_history}"),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])
```
- `system` — the agent's persona and standing instructions ("you are a travel assistant, always check weather first").
- `{chat_history}` — where `ConversationBufferMemory` injects everything said so far.
- `{input}` — the user's current message.
- `{agent_scratchpad}` — **this is the ReAct loop made concrete.** Every time the agent calls a tool, that action and its result get serialized and dropped into this slot before the *next* LLM call, so the model can see its own prior thoughts/actions and avoid repeating them. Without it, a tool-calling agent literally cannot function — it would have amnesia about its own tool calls within the same turn.

### 6.3 `create_tool_calling_agent` + `AgentExecutor`
- `create_tool_calling_agent(llm, tools, prompt)` builds the *definition* of the agent — it wires the LLM's native function/tool-calling capability (the same mechanism behind OpenAI "function calling" or Gemini "function calling") to your specific tools and prompt. It does not run anything by itself.
- `AgentExecutor(agent=..., tools=..., memory=..., verbose=True)` is the *runtime* — it actually drives the ReAct loop: call the LLM → check if it wants to call a tool → if yes, run that Python function → feed the result back into `agent_scratchpad` → call the LLM again → repeat until the LLM returns a final answer or `max_iterations` is hit.
- Real-world analogy: `create_tool_calling_agent` writes the recipe (ingredients = tools, method = prompt); `AgentExecutor` is the chef actually standing in the kitchen executing it, step by step, tasting (observing) as they go.

### 6.4 Memory (`memory/memory.py`)
```python
ConversationBufferMemory(memory_key="chat_history", return_messages=True)
```
- Stores the full, unsummarized conversation and re-injects it as `chat_history` on every call.
- **Trade-off to know for later**: this grows unboundedly — a long conversation eventually blows past the LLM's context window and gets expensive (every past message gets re-sent on every turn). Production systems usually graduate to:
  - `ConversationSummaryMemory` — periodically compresses old turns into a running summary instead of keeping raw text.
  - Vector-store-backed memory — embeds past conversations/facts and retrieves only the relevant ones (semantic search), used for true long-term, cross-session memory (e.g. "remember that Pranav prefers window seats," recalled weeks later).
  - Entity memory — tracks structured facts about specific people/things mentioned, rather than raw transcript.

### 6.5 LLM abstraction (`utils/llm.py`)
```python
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
```
- Every other file imports `llm` from this one place instead of constructing its own model client. This means swapping Gemini for GPT-4 or Claude later is a one-line change here, not a find-and-replace across the whole codebase.
- `temperature=0` means "be as deterministic/consistent as possible" — good for an agent making tool-selection decisions, where you want repeatable reasoning rather than creative variation.
- Real-world parallel: this is the same reason apps use a database *driver* abstraction — swap Postgres for MySQL without rewriting business logic.

### 6.6 Secrets (`.env`)
- API keys go in `.env`, loaded via `python-dotenv`'s `load_dotenv()`, and are never hardcoded into `.py` files.
- **Why this matters, concretely**: if an API key is committed to a public GitHub repo, automated bots scan for leaked keys and can start using (and billing) them within minutes to hours of the push — this has happened repeatedly with leaked OpenAI/AWS keys. `.env` + `.gitignore` is the standard defense.

## 7. LangChain's package split (practical, advanced — this bit you learned by hitting real errors)

LangChain 1.0 restructured the library into separate packages:
- **`langchain`** — now a slim entry point exposing the *new* agent API (`create_agent`), the modern recommended way to build agents.
- **`langchain_classic`** — the *older* API this project actually uses: `create_tool_calling_agent`, `AgentExecutor`, `ConversationBufferMemory`. Kept alive for existing code, but no longer the default import path.
- **`langchain_core`** — framework primitives shared by everything: `@tool`, `ChatPromptTemplate`, base classes.
- **`langchain_community`** — community-maintained integrations (loaders, misc tools).
- **Provider packages** — one per model vendor: `langchain_google_genai` (Gemini), `langchain_openai` (OpenAI), etc.

**Debugging lesson**: when an import that "should" work throws `ImportError`, don't assume the environment is broken — check `pip show <package>` for the installed version and look at that package's own `__init__.py` (`site-packages/<package>/__init__.py`) to see what it currently exports. Library major-version bumps move things between packages far more often than they remove functionality outright.

## 8. Real bugs from this project (and the general lesson each one teaches)

| Bug | Root cause | Lesson |
|---|---|---|
| `create_tool_calling_agent` not found in `langchain.agents` | API moved to `langchain_classic` in LangChain 1.x | Check the installed version before assuming the venv is broken |
| `ModuleNotFoundError` on `agents.travel_agent` | Folder was named `agent` (singular), import said `agents` | Python import paths must match folder names exactly, letter for letter |
| `ValueError: Function must have a docstring` | `@tool`-decorated functions with no docstring | The docstring isn't documentation here — it's functional input the LLM reads |
| `requirements.txt` showing 0 bytes / nothing installed | File was created but never populated | An empty `requirements.txt` isn't a venv bug — `pip install -r` on an empty file installs nothing, silently |
| Empty `GOOGLE_API_KEY` in `.env` | Placeholder left blank | Auth failures downstream often trace back to an unset env var, not the code |

## 9. Where this goes next (advanced roadmap)

- **LangGraph** (already in your `requirements.txt`, not yet used) — a graph-based alternative to `AgentExecutor`. Instead of a fixed reasoning loop, you define explicit nodes/edges, which gives you branching logic, cycles, retries, and **human-in-the-loop approval steps** (e.g. "pause and ask the user to confirm before actually booking the flight"). This is the natural next step once `AgentExecutor`'s single linear loop feels too rigid.
- **RAG (Retrieval-Augmented Generation)** — give the agent a tool backed by a vector database over your own documents, so it can answer questions using private/proprietary knowledge instead of only its training data or hardcoded dicts.
- **Multi-agent systems** — one "orchestrator" agent delegates sub-tasks to specialized agents (e.g. a "flights agent," a "hotels agent"), each with its own tools and prompt, coordinated by a top-level planner.
- **Observability/tracing** (e.g. LangSmith) — logs every Thought/Action/Observation step in production so you can debug *why* an agent made a particular decision, not just see the final output.
- **Guardrails** — validating tool outputs and LLM outputs before acting on them (e.g. don't let the agent "book" something without a confirmation step), rate limiting, and cost tracking on LLM calls.
