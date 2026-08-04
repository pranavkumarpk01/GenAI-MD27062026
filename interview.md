# 🎯 GenAI Interview Prep — 50 Questions with Answers

> A complete interview question bank covering everything in this workspace: **GenAI Fundamentals**, **Python Basics**, **RAG (Retrieval-Augmented Generation)**, **RAG Evaluation**, **AI Agents**, and **FastAPI / Pydantic**.
>
> Questions are ordered **easy → medium** within each topic. Each answer is concise and interview-ready.

---

## 📚 Table of Contents

1. [GenAI Fundamentals](#1-genai-fundamentals) — Q1–Q12
2. [Python Basics](#2-python-basics) — Q13–Q20
3. [RAG — Retrieval-Augmented Generation](#3-rag--retrieval-augmented-generation) — Q21–Q33
4. [RAG Evaluation](#4-rag-evaluation) — Q34–Q40
5. [AI Agents](#5-ai-agents) — Q41–Q46
6. [FastAPI, Pydantic & Deployment](#6-fastapi-pydantic--deployment) — Q47–Q50

---

## 1. GenAI Fundamentals

### Q1. What is the difference between AI, ML, DL, and Generative AI? *(Easy)*
**Answer:** They are nested subsets. **AI** is the broadest field — machines performing tasks that need human-like intelligence. **ML** is a subset of AI where systems *learn patterns from data* instead of being explicitly programmed. **DL** (Deep Learning) is a subset of ML that uses multi-layered neural networks to learn complex representations. **Generative AI** is a subset of DL that *creates new content* (text, images, code, audio) rather than just classifying or predicting.

### Q2. What is a Foundation Model? *(Easy)*
**Answer:** A foundation model is a large model trained on massive, broad, unlabeled data that can be adapted (via prompting or fine-tuning) to many downstream tasks. Examples include GPT, Gemini, LLaMA, and Claude. The key idea is "train once, adapt many times" instead of building a separate model per task.

### Q3. What does a Large Language Model (LLM) actually do at inference time? *(Easy)*
**Answer:** An LLM predicts the **next token** given the previous tokens. It repeatedly generates one token at a time based on probability distributions learned during training, producing coherent text one piece at a time.

### Q4. What are the four stages of the LLM lifecycle? *(Easy)*
**Answer:** **Pre-training** (learn language from huge unlabeled corpora), **Fine-tuning** (specialize on task/domain-specific labeled data), **RAG** (inject external, up-to-date knowledge at query time without retraining), and **Inference** (the deployed model answering user prompts).

### Q5. What is Prompt Engineering? *(Easy)*
**Answer:** The practice of crafting inputs (prompts) to guide an LLM toward the desired output. Good prompts give clear instructions, context, examples, and format expectations to improve accuracy and reduce hallucination — without changing the model's weights.

### Q6. Explain Role-Based (System) Prompting, Few-Shot, and Chain-of-Thought prompting. *(Medium)*
**Answer:**
- **Role-based / System prompting:** Assign the model a persona or role (e.g., "You are a senior legal advisor") to steer tone and expertise.
- **Few-shot prompting:** Provide a few input→output examples so the model infers the pattern before answering.
- **Chain-of-Thought (CoT):** Ask the model to reason step by step ("think step by step"), which improves performance on multi-step reasoning and math tasks.

### Q7. When would you fine-tune a model versus use RAG? *(Medium)*
**Answer:** Use **fine-tuning** when you need to change *behavior, style, or format* or teach a specialized skill the base model lacks — it bakes knowledge into weights. Use **RAG** when you need *fresh, factual, or proprietary knowledge* that changes often; RAG keeps data external so you update the knowledge base instead of retraining. RAG is cheaper to keep current and provides citations; fine-tuning is better for consistent behavior.

### Q8. What are the core pillars of Responsible AI? *(Medium)*
**Answer:** Key pillars include **Fairness & bias mitigation**, **Transparency & explainability**, **Safety & harm prevention**, **Privacy & data protection**, **Accountability**, and **Inclusion & accessibility**. The goal is AI that is trustworthy, equitable, and does not cause harm.

### Q9. API-based LLM vs Local LLM — what are the trade-offs? *(Medium)*
**Answer:** **API-based** (e.g., OpenAI, Gemini) needs no infrastructure, always uses the latest model, and scales easily — but costs per token, sends data to a third party, and needs internet. **Local** (e.g., via Ollama) gives full data privacy, no per-token cost, and offline use — but needs capable hardware (GPU/RAM), manual updates, and often lags frontier quality. Choose local for privacy/cost at scale; API for convenience and top quality.

### Q10. What is Ollama and why is it useful? *(Easy)*
**Answer:** Ollama is a tool for running open-source LLMs (LLaMA, Mistral, etc.) **locally** on your own machine with a simple CLI (`ollama run llama3.2`) and a built-in REST API. It's useful for privacy, offline development, and avoiding per-token API costs.

### Q11. Why are GPUs better than CPUs for running LLMs? *(Medium)*
**Answer:** LLM inference is dominated by **matrix multiplications**, which are massively parallel. A CPU has a few powerful cores optimized for sequential tasks, while a GPU has thousands of smaller cores that perform many multiply-add operations simultaneously. This parallelism maps perfectly onto the linear algebra behind neural networks, making GPUs far faster for both training and inference.

### Q12. What is a hallucination in LLMs and how does RAG help reduce it? *(Medium)*
**Answer:** A hallucination is when an LLM produces confident but factually wrong or fabricated content. RAG reduces hallucination by retrieving relevant, real documents and grounding the model's answer in that retrieved context (often with citations), so the model relies on evidence rather than only its parametric memory.

---

## 2. Python Basics

### Q13. What are the main built-in data types in Python? *(Easy)*
**Answer:** Common ones are `int`, `float`, `str`, `bool`, `list`, `tuple`, `dict`, `set`, and `NoneType`. Lists are ordered and mutable, tuples are ordered and immutable, dicts store key–value pairs, and sets store unique unordered items.

### Q14. What is the difference between a list and a tuple? *(Easy)*
**Answer:** A **list** is mutable (you can add, remove, change elements) and uses `[]`. A **tuple** is immutable (fixed once created) and uses `()`. Tuples are slightly faster and can be used as dictionary keys; lists are better when data changes.

### Q15. What is type casting in Python? *(Easy)*
**Answer:** Converting a value from one type to another using functions like `int()`, `float()`, `str()`, `bool()`, or `list()`. Example: `int("25")` → `25`. It's used to make data compatible for operations, e.g., converting `input()` (always a string) to a number.

### Q16. Explain the difference between `for` and `while` loops. *(Easy)*
**Answer:** A **`for`** loop iterates over a known sequence or range (you generally know how many times it runs). A **`while`** loop repeats as long as a condition stays true (used when the number of iterations isn't known in advance). `break` exits a loop; `continue` skips to the next iteration.

### Q17. What is the difference between arguments and parameters in a function, and what are default arguments? *(Medium)*
**Answer:** **Parameters** are the variable names in the function definition; **arguments** are the actual values passed when calling it. A **default argument** provides a fallback value used when the caller omits it, e.g., `def greet(name="Guest")`. Python also supports positional, keyword, `*args`, and `**kwargs` arguments.

### Q18. What is a class and what does `self` refer to? *(Medium)*
**Answer:** A **class** is a blueprint for creating objects that bundle data (attributes) and behavior (methods). **`self`** refers to the specific instance the method is being called on, letting each object access its own attributes. The `__init__` method is the constructor that runs when an object is created.

### Q19. How does file handling work in Python and why use `with`? *(Medium)*
**Answer:** You open a file with `open("file.txt", "r")` using modes like `r` (read), `w` (write/overwrite), `a` (append). Using **`with open(...) as f:`** is preferred because it automatically closes the file even if an error occurs, preventing resource leaks. Example: `with open("data.txt") as f: content = f.read()`.

### Q20. How do you handle exceptions in Python? *(Medium)*
**Answer:** Use a `try`/`except` block: risky code goes in `try`, and error handling goes in `except <ExceptionType>`. Optional `else` runs if no exception occurred, and `finally` always runs (used for cleanup). This prevents the program from crashing and lets you respond gracefully to errors like `ValueError` or `FileNotFoundError`.

---

## 3. RAG — Retrieval-Augmented Generation

### Q21. What is RAG in simple terms? *(Easy)*
**Answer:** RAG (Retrieval-Augmented Generation) is a technique where, before answering, the system **retrieves** relevant documents from an external knowledge base and feeds them to the LLM as context. The LLM then **generates** an answer grounded in those documents — combining a search engine's knowledge with an LLM's language ability.

### Q22. How does RAG differ from a traditional Q&A system? *(Easy)*
**Answer:** Traditional keyword Q&A matches exact words and returns pre-written answers. RAG uses **semantic (meaning-based) search** via embeddings to find relevant content even with different wording, and an LLM synthesizes a natural-language answer from the retrieved context — handling unseen questions more flexibly.

### Q23. What are the main stages of a RAG ingestion pipeline? *(Medium)*
**Answer:** (1) **Data collection** from sources (PDFs, web, CSV, email), (2) **Text extraction & cleaning**, (3) **Chunking** into smaller passages, (4) **Metadata attachment**, (5) **Embedding generation** (text → vectors), and (6) **Storage** in a vector database for retrieval.

### Q24. What is chunking and why is chunk size important? *(Medium)*
**Answer:** Chunking splits documents into smaller passages before embedding. Chunk size matters because **too large** chunks dilute relevance and may exceed context limits, while **too small** chunks lose context and split ideas. **Overlap** between chunks preserves continuity so a sentence's meaning isn't cut off at boundaries.

### Q25. What is an embedding? *(Easy)*
**Answer:** An embedding is a numerical vector (e.g., 384 or 1536 numbers) that represents the *meaning* of text. Texts with similar meaning have vectors that are close together in vector space, which is what enables semantic search via similarity comparison.

### Q26. What is a vector database and name a few examples. *(Easy)*
**Answer:** A vector database stores embeddings and enables fast **similarity search** (finding nearest vectors to a query). Examples include **Pinecone, Weaviate, FAISS, ChromaDB, Qdrant, and Milvus**. They index high-dimensional vectors so retrieval stays fast even at scale.

### Q27. How is cosine similarity used in retrieval? *(Medium)*
**Answer:** Cosine similarity measures the angle between two vectors, giving a score from -1 to 1 (1 = identical meaning). At query time, the user's question is embedded and compared to stored document vectors; the documents with the highest cosine similarity are retrieved as the most relevant context.

### Q28. What is hybrid search? *(Medium)*
**Answer:** Hybrid search combines **keyword/lexical search (e.g., BM25)** with **semantic/vector search**. Keyword search excels at exact terms (names, codes, acronyms) while vector search captures meaning. Combining them retrieves results that are both literally and semantically relevant, improving recall and precision.

### Q29. What is re-ranking in RAG? *(Medium)*
**Answer:** Re-ranking is a second pass after initial retrieval: a more powerful **cross-encoder** model re-scores the top-K retrieved chunks by how well each truly answers the query, then reorders them. This surfaces the best passages to the top so the LLM gets the most relevant context, improving answer quality.

### Q30. What is metadata filtering and why is it useful? *(Medium)*
**Answer:** Each chunk can be tagged with metadata (source, date, department, author). At query time you can **filter** retrieval by metadata — e.g., only HR documents, or only docs from 2024. This narrows the search space, improves relevance, and enforces access control (e.g., namespace isolation per team).

### Q31. What is query expansion / query rewriting? *(Medium)*
**Answer:** Techniques that reformulate the user's query to improve retrieval. **Query expansion** adds synonyms or related terms; **query rewriting** uses an LLM to generate several alternate phrasings or sub-questions. Retrieving for each variant and merging results captures documents the original wording would have missed.

### Q32. What is semantic caching in RAG? *(Medium)*
**Answer:** Semantic caching stores previous query embeddings and their answers. When a new query is *semantically similar* to a cached one (above a similarity threshold), the cached answer is returned instantly instead of re-running retrieval and generation — cutting latency and cost for repeated or similar questions.

### Q33. What is a self-querying retriever? *(Medium)*
**Answer:** A self-querying retriever uses an LLM to parse a natural-language query into both a **semantic search** part and **structured metadata filters**. For "What leaves do senior employees in India get?", it extracts filters (`level=Senior`, `country=India`) and runs semantic search on the rest — combining filtering with meaning-based retrieval automatically.

---

## 4. RAG Evaluation

### Q34. Why do we need to evaluate a RAG system? *(Easy)*
**Answer:** Because a RAG system has multiple failure points (bad retrieval, insufficient context, wrong generation, unhappy users). Evaluation quantifies where it's failing so you can fix the right stage, prevent hallucinations, track quality over time, and prove reliability before/after changes.

### Q35. Explain Recall vs Precision in retrieval evaluation. *(Medium)*
**Answer:** **Recall** = of all relevant documents that exist, how many did we retrieve? (measures completeness). **Precision** = of the documents we retrieved, how many were actually relevant? (measures accuracy). There's a trade-off: retrieving more docs raises recall but usually lowers precision.

### Q36. What is Hit Rate and MRR? *(Medium)*
**Answer:** **Hit Rate** = the fraction of queries for which at least one relevant document appears in the top-K results. **MRR (Mean Reciprocal Rank)** = the average of 1/(rank of the first relevant result), rewarding systems that place the correct document higher. Both measure retrieval quality, with MRR being rank-sensitive.

### Q37. What is nDCG? *(Medium)*
**Answer:** **nDCG (Normalized Discounted Cumulative Gain)** measures ranking quality by rewarding highly relevant documents appearing near the top and discounting relevance the lower it appears. It's normalized against the ideal ranking (score 0–1), making it useful when results have graded relevance rather than just relevant/not-relevant.

### Q38. What is Faithfulness in generation evaluation? *(Medium)*
**Answer:** Faithfulness measures whether the generated answer is **grounded in the retrieved context** — i.e., every claim is supported by the provided documents and nothing is fabricated. Low faithfulness signals hallucination. It's typically scored as the proportion of answer claims that can be verified against the context.

### Q39. Name and describe two generation quality metrics besides faithfulness. *(Medium)*
**Answer:** **Correctness** — does the answer match the ground-truth/expected answer factually? **Relevancy** — does the answer actually address the user's question? Others include **Completeness** (does it cover all parts of the question?) and **Conciseness** (is it free of unnecessary padding?).

### Q40. How do you measure whether users are actually satisfied with a RAG system? *(Medium)*
**Answer:** Through **user-level signals**: thumbs up/down feedback, explicit satisfaction (CSAT) scores, and behavioral signals like **repeat queries** (a user re-asking the same thing suggests the first answer failed). These complement offline metrics by capturing real-world usefulness.

---

## 5. AI Agents

### Q41. What is an AI agent? *(Easy)*
**Answer:** An AI agent is a system built around an LLM that can **reason, decide, and take actions** using tools to achieve a goal — rather than just responding once. It observes results, plans next steps, and loops until the task is complete, giving the LLM the ability to *act*, not just *talk*.

### Q42. How does an agent differ from a chatbot and from simple automation? *(Easy)*
**Answer:** A **chatbot** just replies to messages conversationally. **Automation** follows fixed, predefined rules/scripts. An **agent** dynamically decides *which* actions/tools to use based on the goal and intermediate results — it's flexible and goal-driven rather than hard-coded or purely conversational.

### Q43. What is the ReAct pattern? *(Medium)*
**Answer:** **ReAct = Reasoning + Acting.** The agent alternates between **Thought** (reason about what to do), **Action** (call a tool), and **Observation** (read the tool's result), looping until it can produce a final answer. This interleaving lets the LLM plan, use tools, and adjust based on real feedback.

### Q44. What are "tools" in the context of an agent? *(Easy)*
**Answer:** Tools are functions the agent can call to interact with the outside world — e.g., a weather API, a web search, a flight lookup, or a calculator. Each tool has a name, description, and input schema so the LLM knows when and how to call it. Tools extend the agent beyond its frozen training knowledge.

### Q45. Why does an agent need memory, and how can it be implemented? *(Medium)*
**Answer:** Memory lets the agent remember past turns so conversation stays coherent and context carries across messages. Short-term memory holds the current chat; persistent memory (e.g., a **SQLite database keyed by session_id**) stores history so it survives restarts. Without memory, each query would be treated in isolation.

### Q46. What is the role of a framework like LangChain in building agents? *(Medium)*
**Answer:** LangChain provides building blocks — LLM abstractions, prompt templates, tool integration, an **AgentExecutor** that runs the reason-act loop, and memory backends — so you don't wire the ReAct loop by hand. It standardizes connecting an LLM to tools, prompts, and memory, speeding up agent development.

---

## 6. FastAPI, Pydantic & Deployment

### Q47. What is FastAPI and what is Uvicorn? *(Easy)*
**Answer:** **FastAPI** is a modern, high-performance Python web framework for building APIs, with automatic interactive docs (Swagger UI) and built-in validation. **Uvicorn** is the ASGI server that actually runs the FastAPI app on a port and handles incoming requests asynchronously.

### Q48. What is Pydantic and why is it used with FastAPI? *(Medium)*
**Answer:** Pydantic is a data-validation library. You define a model (a class of typed fields), and FastAPI uses it to **validate incoming request data**. If the client sends data of the wrong shape or type, the request is rejected *before* it reaches your endpoint logic — preventing malformed data from hitting your database. It also auto-generates clear error messages and API docs.

### Q49. What problem occurs if you accept a raw `dict` instead of a Pydantic model? *(Medium)*
**Answer:** Using a plain `dict` means FastAPI accepts **any** payload shape or type — e.g., a string for `age` or missing fields. That bad data flows straight into your logic or database, causing corrupt records and hard-to-debug errors. A Pydantic model enforces the expected schema and blocks invalid requests early.

### Q50. How is MongoDB set up with Docker for a FastAPI app? *(Medium)*
**Answer:** Install Docker, then **pull the official image** (`docker pull mongo`) and **run a container** exposing MongoDB's port (e.g., `docker run -d -p 27017:27017 mongo`). Docker isolates the database in a container so it runs consistently across environments without a manual local install. The FastAPI app then connects to `localhost:27017`, and dependencies are installed via `pip install -r requirements.txt`.

---

## ✅ Quick Revision Checklist

- **GenAI:** AI⊃ML⊃DL⊃GenAI, foundation models, LLM lifecycle (pretrain→fine-tune→RAG→inference), prompt patterns, responsible AI, API vs local, GPU parallelism.
- **Python:** data types, list vs tuple, type casting, loops, functions & `self`, file handling with `with`, `try/except`.
- **RAG:** ingestion pipeline, chunking + overlap, embeddings, vector DBs, cosine similarity, hybrid search, re-ranking, metadata filtering, query rewriting, semantic caching.
- **RAG Eval:** recall/precision, hit rate, MRR, nDCG, faithfulness, correctness, relevancy, user satisfaction.
- **Agents:** ReAct loop, tools, memory, LangChain AgentExecutor.
- **FastAPI:** Uvicorn/ASGI, Pydantic validation, MongoDB + Docker.

*Good luck! 🚀*
