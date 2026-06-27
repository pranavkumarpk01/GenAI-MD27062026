# 🤖 Introduction to Generative AI — Complete Notes

> **Module:** Introduction to GenAI  
> **Level:** Beginner → Intermediate  
> **Topics:** AI/ML/DL/GenAI · Foundation Models · LLM Lifecycle · Prompt Engineering · Responsible AI · API vs Local LLMs · Ollama · CPU vs GPU

---

## 📌 Table of Contents

1. [AI vs ML vs DL vs GenAI](#1-ai-vs-ml-vs-dl-vs-genai)
2. [Evolution of Foundation Models](#2-evolution-of-foundation-models)
3. [LLM Lifecycle](#3-llm-lifecycle-pretrain--fine-tune--rag--inference)
4. [Prompt Patterns](#4-prompt-patterns)
5. [Responsible AI Concepts](#5-responsible-ai-concepts)
6. [API vs Local LLM Comparison](#6-api-vs-local-llm-comparison)
7. [Running Ollama Locally](#7-running-ollama-locally)
8. [CPU vs GPU Fundamentals](#8-cpu-vs-gpu-fundamentals)
9. [Interview Questions](#9-interview-questions)

---

## 1. AI vs ML vs DL vs GenAI

### 🔷 The Hierarchy

```
┌─────────────────────────────────────────────────────┐
│                   ARTIFICIAL INTELLIGENCE            │
│  ┌───────────────────────────────────────────────┐  │
│  │            MACHINE LEARNING                   │  │
│  │  ┌─────────────────────────────────────────┐  │  │
│  │  │          DEEP LEARNING                  │  │  │
│  │  │  ┌───────────────────────────────────┐  │  │  │
│  │  │  │     GENERATIVE AI                 │  │  │  │
│  │  │  │  (LLMs, Diffusion, GANs, etc.)    │  │  │  │
│  │  │  └───────────────────────────────────┘  │  │  │
│  │  └─────────────────────────────────────────┘  │  │
│  └───────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────┘
```

---

### 🤖 Artificial Intelligence (AI)

**Definition:**  
AI is the broad science of making machines simulate human intelligence — reasoning, understanding language, recognizing patterns, and making decisions.

**Example:**  
A chess-playing program that beats grandmasters (Deep Blue, 1997).

**Real-World Scenarios:**
- Google Maps predicting traffic and rerouting
- Netflix recommending shows based on your history
- Hospital systems flagging abnormal X-rays for radiologist review

---

### 📊 Machine Learning (ML)

**Definition:**  
A subset of AI where machines **learn patterns from data** without being explicitly programmed for every rule. Models improve with experience.

**Key Types:**

| Type | Description | Example |
|------|-------------|---------|
| Supervised | Learns from labelled data | Spam email classification |
| Unsupervised | Finds hidden patterns in unlabelled data | Customer segmentation |
| Reinforcement | Learns by reward/penalty signals | Game-playing agents, robots |

**Example:**  
A bank's fraud detection system trained on millions of past transactions to flag suspicious activity.

**Real-World Scenarios:**
- Credit scoring at banks (CIBIL, FICO)
- Product demand forecasting in retail (Flipkart, Amazon)
- Predictive maintenance in manufacturing (detecting machine failure before it happens)

---

### 🧠 Deep Learning (DL)

**Definition:**  
A subset of ML using **multi-layered artificial neural networks** (inspired by the human brain) to learn complex representations from large datasets automatically.

**Architecture Diagram:**

```
Input Layer    Hidden Layers       Output Layer
   [X1]  ──►  [N]─[N]─[N]  ──►   [Prediction]
   [X2]  ──►  [N]─[N]─[N]  ──►
   [X3]  ──►  [N]─[N]─[N]  ──►
   
   Each [N] = Neuron with weights + activation function
```

**Why Deep Learning > Classical ML?**
- Automatically extracts features (no manual feature engineering)
- Handles unstructured data: images, audio, text, video
- Scales massively with more data + GPU compute

**Example:**  
Face Unlock on your phone — a CNN (Convolutional Neural Network) maps your face geometry to a unique vector and compares it at login.

**Real-World Scenarios:**
- Google Translate (seq2seq models)
- Tesla Autopilot (object detection via CNNs)
- Siri / Alexa (speech recognition via RNNs/Transformers)
- Medical imaging (tumour detection in MRI scans)

---

### ✨ Generative AI (GenAI)

**Definition:**  
A class of deep learning models that can **generate new content** — text, images, audio, video, code — that didn't exist before, by learning the statistical patterns of training data.

**Key Generative Architectures:**

| Architecture | Full Form | Used For |
|---|---|---|
| LLM | Large Language Model | Text, code, reasoning |
| GAN | Generative Adversarial Network | Image synthesis |
| VAE | Variational Autoencoder | Image generation, compression |
| Diffusion Model | — | High-quality image/video generation |

**Example:**  
ChatGPT generating a complete Python script from a plain English description.

**Real-World Scenarios:**
- GitHub Copilot auto-completing code as you type
- Midjourney/DALL·E creating product images for e-commerce
- Suno AI composing full songs from a text prompt
- Adobe Firefly generating backgrounds in Photoshop
- Synthesia creating AI avatar training videos for corporates

---

### 🧾 Quick Comparison Table

| Dimension | AI | ML | DL | GenAI |
|-----------|----|----|----|----|
| Scope | Broadest | Subset of AI | Subset of ML | Subset of DL |
| Data Needed | Varies | Structured | Large + Unstructured | Massive (billions of tokens) |
| Output | Decisions | Predictions | Classifications/Embeddings | New Content |
| Compute | Low–High | Medium | High (GPU) | Very High (GPU clusters) |
| Example Tool | Rule-based chatbot | Scikit-learn | TensorFlow/PyTorch | GPT-4, Gemini, Claude |

---

## 2. Evolution of Foundation Models

### 🔷 What is a Foundation Model?

**Definition:**  
A large-scale model trained on **vast, diverse datasets** (text, images, code, etc.) that can be adapted to a **wide range of downstream tasks** with minimal fine-tuning. The term was coined by Stanford HAI in 2021.

> Think of it as a "base" model — like a Swiss Army knife — that can be adapted for many jobs.

---

### 📅 Timeline of Foundation Model Evolution

```
1950s─────1980s──────2013──────2017──────2018──────2019──────2020──────2022──────2023──────2024
  │           │         │         │         │         │         │         │         │         │
Perceptron  Backprop  Word2Vec  Transformer BERT    GPT-2    GPT-3    ChatGPT  GPT-4/    Gemini/
(Rosenblatt)(Rumelhart)(Mikolov) (Attention  (Google) (OpenAI) (175B    (OpenAI) Claude-3  Llama-3/
            RNNs appear is All    params)              params)           Llama-2  Mixtral
                       You Need)
```

---

### 🗓️ Key Milestones Explained

#### 📌 Word2Vec (2013) — Google
**What:** Learned word embeddings — representing words as dense numerical vectors so that "King − Man + Woman ≈ Queen".  
**Significance:** First time semantic meaning was captured mathematically.

#### 📌 Transformer Architecture (2017) — Google Brain
**Paper:** *"Attention Is All You Need"* — Vaswani et al.  
**What:** Replaced RNNs with **self-attention mechanisms**, enabling parallel processing of entire sequences.  
**Why it matters:** This is the architectural backbone of ALL modern LLMs.

```
Transformer Block:
  Input Tokens
       ↓
  [Embedding Layer]
       ↓
  [Multi-Head Self-Attention]  ← "Which words should I focus on?"
       ↓
  [Feed-Forward Network]
       ↓
  [Layer Norm + Residual]
       ↓
  Output Logits → Next Token Prediction
```

#### 📌 BERT (2018) — Google
- **Bidirectional** — reads context from both left and right
- Pre-trained on: Masked Language Modelling + Next Sentence Prediction
- Best for: Classification, NER, Q&A (understanding tasks)

#### 📌 GPT-2 (2019) → GPT-3 (2020) — OpenAI
- **Unidirectional** (left to right) — auto-regressive generation
- GPT-3: **175 billion parameters**, few-shot learning capability
- Showed emergent abilities: translation, coding, reasoning — without task-specific training

#### 📌 ChatGPT (2022) — OpenAI
- GPT-3.5 + **RLHF** (Reinforcement Learning from Human Feedback)
- Aligned to be helpful, harmless, honest
- Reached 100 million users in 2 months — fastest product adoption in history

#### 📌 GPT-4 / Claude / Gemini / Llama (2023–2024)
- Multimodal (text + image + audio + video)
- Longer context windows (128K → 1M+ tokens)
- Open-source alternatives: Meta's Llama 2/3, Mistral, Falcon

---

### 🌍 Real-World Scenario
A healthcare company uses **BERT** fine-tuned on medical literature (BioBERT) to extract diagnoses from clinical notes. Meanwhile, their patient chatbot runs on **GPT-4** via API for natural conversations — two foundation models, two different jobs, same foundation model paradigm.

---

## 3. LLM Lifecycle: Pretrain → Fine-Tune → RAG → Inference

### 🔷 Overview

```
┌────────────────────────────────────────────────────────────────────────┐
│                         LLM LIFECYCLE                                  │
│                                                                        │
│  [Raw Internet Data]                                                   │
│         │                                                              │
│         ▼                                                              │
│  ┌─────────────┐     ┌─────────────┐     ┌──────────┐     ┌────────┐  │
│  │  PRE-TRAIN  │────►│  FINE-TUNE  │────►│   RAG    │────►│INFER  │  │
│  │ (learn the  │     │(adapt to    │     │(add live │     │(serve │  │
│  │  world)     │     │ your domain)│     │knowledge)│     │users) │  │
│  └─────────────┘     └─────────────┘     └──────────┘     └────────┘  │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

---

### 🟦 Stage 1: Pre-Training

**Definition:**  
Training a model from scratch on **massive, diverse text corpora** to learn language, facts, reasoning, and world knowledge via next-token prediction.

**Data Sources:**
- Common Crawl (web scrape)
- Wikipedia, Books, GitHub, ArXiv, StackOverflow

**Objective:** Predict the next token given all previous tokens.

```
Input:  "The capital of France is ___"
Target: "Paris"

Loss = Cross-Entropy(predicted_token, actual_token)
Model updates weights via backpropagation + gradient descent
```

**Scale & Cost:**
- GPT-3: ~$4.6 million in compute
- Llama 3 70B: trained on 15 trillion tokens
- Requires thousands of A100/H100 GPUs

**Real-World Scenario:**  
Meta spent months and millions pre-training Llama 3 on cluster of thousands of GPUs. You download the result in 5 minutes via `ollama pull llama3`.

---

### 🟩 Stage 2: Fine-Tuning

**Definition:**  
Taking a pre-trained model and continuing training on a **smaller, task-specific or domain-specific dataset** to specialise its behaviour.

**Types of Fine-Tuning:**

| Type | Description | Use Case |
|------|-------------|----------|
| Full Fine-Tuning | Update all weights | Max accuracy, max cost |
| LoRA | Update low-rank adapter matrices only | Efficient, popular |
| QLoRA | LoRA + 4-bit quantisation | Run on consumer GPUs |
| RLHF | Reward model + PPO to align behaviour | ChatGPT's secret sauce |
| Instruction Tuning | Supervised on (instruction, response) pairs | Flan-T5, Alpaca |

**Example:**  
A legal tech startup fine-tunes Llama 3 on 50,000 Indian court judgements. The model now understands legal jargon, IPC sections, and can draft contracts — something the base model couldn't do reliably.

**Real-World Scenario:**  
HealthEdge (your context!) might fine-tune a base LLM on clinical EDI 837/835 data so it understands healthcare billing terminology natively, without needing it in every prompt.

---

### 🟨 Stage 3: RAG (Retrieval-Augmented Generation)

**Definition:**  
Augmenting LLM responses by **retrieving relevant documents** from an external knowledge base at inference time and injecting them into the prompt context.

**Why RAG?**  
LLMs have a **knowledge cutoff** and can hallucinate. RAG gives them access to up-to-date, domain-specific, private knowledge.

**RAG Architecture:**

```
User Query: "What is our refund policy for Plan B subscribers?"
      │
      ▼
┌─────────────┐        ┌──────────────────┐
│  Embedding  │──────► │  Vector Database │
│   Model     │        │  (pgvector,      │
│(MiniLM etc) │◄──────►│   Pinecone,      │
└─────────────┘  Top-K │   ChromaDB)      │
      │          chunks └──────────────────┘
      ▼
┌─────────────────────────────────────────┐
│         AUGMENTED PROMPT                │
│  Context: [retrieved chunks]            │
│  Question: [user query]                 │
│  Instruction: Answer only from context  │
└─────────────────────────────────────────┘
      │
      ▼
   LLM → Grounded Answer
```

**Real-World Scenario:**  
A customer support bot for an e-commerce company uses RAG over their product catalogue (50,000 SKUs). When a user asks "Does the Nike Air Max 270 come in size 13?", the system fetches the relevant product doc and the LLM answers accurately — no hallucination.

---

### 🟥 Stage 4: Inference

**Definition:**  
The process of running a trained model to generate outputs for new inputs — this is what end-users interact with.

**Key Inference Concepts:**

| Concept | Definition |
|---------|-----------|
| Temperature | Controls randomness (0 = deterministic, 1 = creative) |
| Top-K / Top-P | Sampling strategies to control output diversity |
| Max Tokens | Limits response length |
| Streaming | Send tokens as they're generated (better UX) |
| Batching | Process multiple requests simultaneously for throughput |
| Quantisation | Reduce model precision (FP16 → INT4) to lower memory/cost |

**Deployment Options:**
- **Cloud API:** OpenAI, Anthropic, Google Vertex AI
- **Self-hosted:** Ollama, vLLM, TGI (Text Generation Inference)
- **Edge:** Llama.cpp on mobile/laptop

**Real-World Scenario:**  
Your Agentic RAG system at HealthEdge serves inference via a Kubernetes pod. Prometheus tracks latency per token; Grafana shows P95 < 800ms SLA.

---

## 4. Prompt Patterns

### 🔷 What is Prompt Engineering?

**Definition:**  
The practice of **designing and structuring input text (prompts)** to guide LLM behaviour toward desired outputs — without changing the model weights.

> Prompt engineering is to LLMs what SQL is to databases — the primary interface.

---

### 🟦 Pattern 1: Role-Based Prompting (System Prompting)

**Definition:**  
Assigning the LLM a **persona or role** that constrains its style, expertise, and tone throughout the conversation.

**Structure:**
```
SYSTEM: You are [ROLE]. You [BEHAVIOUR RULES].
USER: [actual question]
```

**Example 1 — Expert Role:**
```
SYSTEM: You are a senior cardiologist with 20 years of experience.
        Explain medical conditions in simple terms for patients.
        Always recommend consulting a doctor for treatment decisions.

USER: What is atrial fibrillation?
```

**Example 2 — Code Reviewer:**
```
SYSTEM: You are a strict Python code reviewer. 
        Focus on: performance, security, PEP8 compliance.
        Respond ONLY with issues found and suggested fixes.

USER: [paste code here]
```

**Real-World Scenario:**  
A legal SaaS platform uses role prompting to make their LLM behave as "a senior Indian corporate lawyer" — this constrains it to use Indian legal terminology, cite Indian statutes, and avoid giving generic international advice.

---

### 🟩 Pattern 2: Few-Shot Prompting

**Definition:**  
Providing **2–10 input-output examples** within the prompt so the model learns the pattern and applies it to a new input — no training required.

**Structure:**
```
[Example 1 Input] → [Example 1 Output]
[Example 2 Input] → [Example 2 Output]
[Example 3 Input] → [Example 3 Output]
[New Input] → ?
```

**Example — Sentiment Classification:**
```
Classify the sentiment of these customer reviews:

Review: "The product is amazing, exceeded my expectations!" → Positive
Review: "Delivery was late and packaging was damaged." → Negative  
Review: "It's okay, nothing special but does the job." → Neutral

Review: "Absolutely love this! Will definitely buy again." → ?
```
**Model Output:** `Positive`

**Example — Entity Extraction:**
```
Extract the city and date from the sentence:

Sentence: "The conference will be held in Mumbai on March 15th." 
Output: {"city": "Mumbai", "date": "March 15th"}

Sentence: "Join us in Bangalore for the summit on July 4th."
Output: {"city": "Bangalore", "date": "July 4th"}

Sentence: "The event is scheduled in Hyderabad on December 20th."
Output: ?
```

**Real-World Scenario:**  
An invoice processing pipeline uses few-shot prompting to teach the LLM to extract vendor name, amount, date, and GST number from unstructured PDF invoices — 3 example extractions in the prompt, consistent JSON output every time.

---

### 🟨 Pattern 3: Chain-of-Thought (CoT) Prompting

**Definition:**  
Prompting the model to **show its reasoning step by step** before giving the final answer. This dramatically improves accuracy on complex reasoning, math, and logic tasks.

**Why it works:**  
Generating intermediate reasoning steps forces the model to allocate more compute tokens to "thinking" before answering — mimicking how humans solve hard problems.

**Types:**

| Type | How | When to Use |
|------|-----|-------------|
| Zero-Shot CoT | Add "Let's think step by step." | Quick, no examples needed |
| Few-Shot CoT | Provide examples WITH reasoning shown | Complex tasks needing precise format |
| Auto-CoT | LLM generates its own chain automatically | Advanced pipelines |

**Example — Zero-Shot CoT:**
```
Q: A hospital has 3 wards. Each ward has 12 beds. 
   75% are occupied. How many free beds are there?

A: Let's think step by step.
   1. Total beds = 3 × 12 = 36
   2. Occupied = 75% of 36 = 27
   3. Free beds = 36 - 27 = 9
   
   Answer: 9 free beds.
```

**Example — Few-Shot CoT:**
```
Q: If I have 5 apples and give away 2, then buy 4 more, how many do I have?
A: Start with 5. Subtract 2 → 3. Add 4 → 7. Answer: 7.

Q: A store had 100 items, sold 30%, restocked 20 units. How many items?
A: Start with 100. Sold 30% → 30 items sold → 70 left. 
   Add 20 → 90 items. Answer: 90.

Q: A train has 200 seats. 40% are reserved, 50 are occupied by standby 
   passengers. How many seats are freely available?
A: ?
```

**Real-World Scenario:**  
LangGraph-based agentic systems (like your Travel AI Assistant) implicitly use CoT — the ReAct pattern (Reason + Act) is structured CoT: the agent reasons about what tool to call, calls it, observes the result, reasons again, and repeats.

---

### 🧩 Combining All Three Patterns

```
SYSTEM: You are a senior financial analyst specializing in Indian equity markets.  ← Role
        Always show your calculation steps before concluding.                      ← CoT instruction

Example 1: [P/E ratio calculation with steps shown]                               ← Few-shot
Example 2: [EPS calculation with steps shown]

USER: Calculate the intrinsic value of a stock with EPS=45, 
      growth rate=12%, and discount rate=10% for 5 years.
```

---

## 5. Responsible AI Concepts

### 🔷 Definition

**Responsible AI** is the practice of designing, developing, and deploying AI systems that are **safe, fair, transparent, accountable, and beneficial** — minimising harms to individuals and society.

---

### 🧱 Core Pillars

```
┌──────────────────────────────────────────────────────────────────┐
│                    RESPONSIBLE AI PILLARS                        │
│                                                                  │
│  ⚖️  FAIRNESS    🔍 TRANSPARENCY    🔒 PRIVACY    🛡️ SAFETY      │
│  📋 ACCOUNTABILITY   🌍 INCLUSION   ♻️ SUSTAINABILITY            │
└──────────────────────────────────────────────────────────────────┘
```

---

### ⚖️ 1. Fairness & Bias

**Definition:**  
AI systems should not discriminate against individuals or groups based on race, gender, religion, age, disability, or other protected attributes.

**Types of Bias:**

| Bias Type | Description | Example |
|-----------|-------------|---------|
| Data Bias | Training data over/under-represents groups | Facial recognition fails on dark skin |
| Label Bias | Human annotators bring prejudices | Resume screener penalises women's colleges |
| Feedback Bias | RLHF raters skew toward certain styles | Model prefers "authoritative" sounding answers |
| Deployment Bias | Model used in context it wasn't designed for | Medical model used on different population |

**Real-World Scenario:**  
Amazon built an AI hiring tool trained on 10 years of resumes. Since tech was male-dominated, it learned to downgrade resumes mentioning "women's" (as in women's chess club). They scrapped it in 2018.

---

### 🔍 2. Transparency & Explainability

**Definition:**  
Users and stakeholders should be able to understand **how and why** an AI system made a decision — especially in high-stakes contexts.

**Techniques:**
- **LIME:** Local Interpretable Model-Agnostic Explanations
- **SHAP:** SHapley Additive exPlanations (feature importance scores)
- **Attention Visualisation:** Show which tokens the model focused on
- **Prompt Transparency:** Disclose when users are talking to AI

**Real-World Scenario:**  
An Indian bank uses ML to approve/reject loans. RBI guidelines now require explainability — the model must output "Your loan was rejected because your debt-to-income ratio (0.72) exceeds our threshold (0.50)" — not just a yes/no black box.

---

### 🛡️ 3. Safety & Harm Prevention

**Definition:**  
AI systems must avoid producing outputs that cause **physical, psychological, financial, or societal harm**.

**Safety Mechanisms in LLMs:**
- **RLHF (Reinforcement Learning from Human Feedback):** Train models to prefer safe, helpful responses
- **Constitutional AI (Anthropic):** Model critiques its own outputs against a set of principles
- **Guardrails:** Input/output filters (Llama Guard, Azure Content Safety)
- **Red Teaming:** Adversarial testing to find jailbreaks and failure modes

**Categories of Harm:**
- Misinformation / Hallucination
- Hate speech / Toxic content
- CBRN (Chemical, Biological, Radiological, Nuclear) information
- Privacy violations (PII leakage)
- Deepfakes and synthetic media misuse

---

### 🔒 4. Privacy & Data Protection

**Definition:**  
AI systems must handle personal data in compliance with privacy regulations and avoid leaking sensitive information.

**Relevant Regulations:**

| Law | Region | Key Requirement |
|-----|--------|-----------------|
| GDPR | EU | Right to explanation, data deletion |
| DPDP Act 2023 | India | Consent for data processing |
| CCPA | California, USA | Right to opt-out of data sale |
| HIPAA | USA | Health data protection |

**Real-World Scenario:**  
If you prompt ChatGPT with patient data at a hospital, that data may be used for training (unless enterprise tier). Responsible AI practice: use on-premise/local LLMs (like Ollama) for sensitive healthcare data — no data leaves your servers.

---

### 📋 5. Accountability

**Definition:**  
There must be clear ownership and responsibility for AI system decisions — humans remain accountable, not the model.

**Practices:**
- Maintain **model cards** (documentation of training data, limitations, intended use)
- **Audit trails** for high-stakes AI decisions
- **Human-in-the-loop** for irreversible actions (medical diagnosis, judicial decisions)
- Incident response plans for AI failures

---

### 🌍 6. Inclusion & Accessibility

**Definition:**  
AI systems should work equitably across languages, cultures, abilities, and demographics.

**Real-World Scenario:**  
Your Kannada AI Instagram page directly addresses this — making AI education accessible in regional Indian languages, countering the English-language bias in AI content.

---

## 6. API vs Local LLM Comparison

### 🔷 What is an API-based LLM?

Accessing a model **hosted by a provider** (OpenAI, Anthropic, Google) via HTTP requests. You send prompts, they return completions. You never touch the model weights.

### 🔷 What is a Local LLM?

Running the model **on your own hardware** — laptop, workstation, or on-premise server. Model weights downloaded and executed locally (via Ollama, llama.cpp, vLLM).

---

### 📊 Full Comparison Table

| Dimension | API LLM (e.g., GPT-4, Claude) | Local LLM (e.g., Llama 3 via Ollama) |
|-----------|-------------------------------|--------------------------------------|
| **Setup** | API key + one line of code | Download model, install runtime |
| **Cost** | Pay per token (usage-based) | Hardware cost only, zero per-query cost |
| **Privacy** | Data sent to 3rd party servers | Data never leaves your machine |
| **Model Quality** | SOTA (state-of-the-art) | Smaller, slightly less capable |
| **Latency** | Network round-trip (~500ms) | Can be faster on good hardware |
| **Customisation** | Limited (system prompt only) | Full control (quantise, fine-tune) |
| **Offline Use** | ❌ Requires internet | ✅ Works fully offline |
| **Scaling** | Auto-scales (provider handles infra) | You manage infra, GPU memory caps |
| **Compliance** | Depends on provider's data policy | Full compliance possible (HIPAA, etc.) |
| **Updates** | Provider pushes updates silently | You choose when to update |
| **Best For** | Production apps, best quality | Privacy-sensitive data, cost reduction, offline |

---

### 💰 Cost Example

```
Scenario: 10,000 users × 500 tokens/day = 5,000,000 tokens/day

GPT-4o:    $5 per 1M tokens → $25/day → $750/month
GPT-4o mini: $0.15 per 1M tokens → $0.75/day → $22.50/month
Llama 3 (local): $0/query → server cost only (e.g., $200/month for a GPU VM)
```

At scale, local LLMs become dramatically cheaper.

---

### 🎯 Decision Framework

```
Does your data contain PII/PHI/confidential info?
         │
        YES ──► Local LLM (Ollama, vLLM)
         │
        NO
         │
Do you need best-in-class quality?
         │
        YES ──► API LLM (GPT-4o, Claude Sonnet)
         │
        NO
         │
High volume / cost sensitive?
         │
        YES ──► Local LLM or smaller API model (GPT-4o-mini, Haiku)
         │
        NO ──► API LLM for simplicity
```

---

### 🌍 Real-World Scenario

**Healthcare (HealthEdge use case):**  
Patient EDI data is ePHI — sending it to OpenAI violates HIPAA without a BAA. Solution: Run Llama 3 locally via Ollama on your Kubernetes cluster. Zero data egress. Full HIPAA compliance. Your Agentic RAG pipeline stays entirely on-premises.

**Startup building a chatbot:**  
Early-stage? Use Claude API — zero infra overhead, best quality, pay-as-you-go. Once you hit 10M tokens/month, evaluate migration to local.

---

## 7. Running Ollama Locally

### 🔷 What is Ollama?

**Definition:**  
Ollama is an **open-source tool** that lets you download, manage, and run large language models locally on your machine — with a single command. It packages model weights + runtime into a simple CLI and REST API.

> Think of it as "Docker for LLMs" — same UX simplicity, but for AI models.

**Supported Platforms:** macOS, Linux, Windows  
**GitHub:** https://github.com/ollama/ollama

---

### ⚙️ Installation

```bash
# macOS / Linux (one-liner)
curl -fsSL https://ollama.com/install.sh | sh

# Verify installation
ollama --version
```

On **Windows:** Download the installer from https://ollama.com/download

---

### 🚀 Running Your First Model

```bash
# Pull and run Llama 3.2 (3B — works on 8GB RAM)
ollama run llama3.2

# Pull and run Mistral 7B
ollama run mistral

# Pull and run a coding model
ollama run codellama

# Pull without running
ollama pull llama3.2

# List downloaded models
ollama list

# Remove a model
ollama rm llama3.2
```

---

### 🌐 Ollama REST API

Ollama exposes a local API on `http://localhost:11434`

```bash
# One-shot completion
curl http://localhost:11434/api/generate \
  -d '{
    "model": "llama3.2",
    "prompt": "Explain RAG in 2 sentences.",
    "stream": false
  }'
```

**Python Integration:**
```python
import requests

def ask_ollama(prompt, model="llama3.2"):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": model,
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]

answer = ask_ollama("What is the capital of Karnataka?")
print(answer)  # Bengaluru
```

**With LangChain:**
```python
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3.2")
response = llm.invoke("Explain LLM in simple terms.")
print(response)
```

---

### 📦 Popular Models & System Requirements

| Model | Parameters | VRAM / RAM Needed | Good For |
|-------|-----------|-------------------|----------|
| llama3.2 | 3B | 4 GB | General use, low-end hardware |
| llama3.1 | 8B | 8 GB | Good balance of quality/speed |
| mistral | 7B | 8 GB | Fast, good reasoning |
| codellama | 7B | 8 GB | Code generation |
| llava | 7B | 8 GB | Vision + text (multimodal) |
| llama3.1 | 70B | 48 GB | Near GPT-4 quality |
| deepseek-coder | 6.7B | 8 GB | Code focused |

---

### 🏗️ Ollama Architecture

```
┌───────────────────────────────────────────────────┐
│                  YOUR MACHINE                     │
│                                                   │
│   CLI / Python / LangChain                        │
│          │                                        │
│          ▼                                        │
│   ┌─────────────────┐                             │
│   │  Ollama Server  │ ← localhost:11434           │
│   │  (REST API)     │                             │
│   └────────┬────────┘                             │
│            │                                      │
│            ▼                                      │
│   ┌─────────────────┐                             │
│   │  llama.cpp      │ ← quantised model runtime   │
│   │  (inference     │                             │
│   │   engine)       │                             │
│   └────────┬────────┘                             │
│            │                                      │
│            ▼                                      │
│   ┌─────────────────┐                             │
│   │  Model Weights  │ ← ~/.ollama/models/         │
│   │  (.gguf files)  │                             │
│   └─────────────────┘                             │
└───────────────────────────────────────────────────┘
```

---

### 💡 Pro Tips

```bash
# See what Ollama is doing (GPU/CPU usage)
ollama ps

# Run with specific system prompt
ollama run llama3.2 "You are a Kannada language tutor. Respond in Kannada."

# Use a Modelfile for custom models
cat > Modelfile << 'EOF'
FROM llama3.2
SYSTEM "You are an expert in Indian healthcare billing and ICD-10 codes."
PARAMETER temperature 0.3
EOF

ollama create healthedge-assistant -f Modelfile
ollama run healthedge-assistant
```

---

### 🌍 Real-World Scenario

Your **Travel AI Assistant** project (LangGraph + ReAct + SerpAPI) uses Ollama as the local LLM backend. Instead of paying OpenAI per tool call, every reasoning step — which tool to call, how to interpret search results, final answer synthesis — runs locally for free. This is exactly how production-grade agentic systems can be prototyped and tested without API costs.

---

## 8. CPU vs GPU Fundamentals

### 🔷 Core Difference

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│   CPU (Central Processing Unit)    GPU (Graphics Processing Unit)  │
│                                                                     │
│   ┌──┐ ┌──┐ ┌──┐ ┌──┐            ┌─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┐   │
│   │C1│ │C2│ │C3│ │C4│            │ │ │ │ │ │ │ │ │ │ │ │ │ │   │
│   └──┘ └──┘ └──┘ └──┘            ├─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┤   │
│                                   │ │ │ │ │ │ │ │ │ │ │ │ │ │   │
│   4–64 powerful cores             ├─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┤   │
│   Complex sequential tasks        │ │ │ │ │ │ │ │ │ │ │ │ │ │   │
│                                   └─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┘   │
│                                   1,000–16,000+ smaller cores      │
│                                   Massively parallel tasks         │
└─────────────────────────────────────────────────────────────────────┘
```

---

### 🔵 CPU (Central Processing Unit)

**Definition:**  
The general-purpose processor of a computer. Designed for **sequential, complex, low-latency** tasks. A few very powerful cores with sophisticated control logic, large cache, and branch prediction.

**Specs Example (Intel i9-13900K):**
- 24 cores (8 P-cores + 16 E-cores)
- Clock speed: up to 5.8 GHz
- Cache: 36 MB L3
- Good at: OS scheduling, database queries, web servers, conditional logic

**How LLMs run on CPU:**
- Slower token generation (5–15 tokens/sec for 7B models)
- Works via llama.cpp with quantised models (INT4/INT8)
- No VRAM limit — uses system RAM (32/64 GB accessible)
- Good for: development, testing, light use

```bash
# Force Ollama to use CPU only
CUDA_VISIBLE_DEVICES="" ollama run llama3.2
```

---

### 🟢 GPU (Graphics Processing Unit)

**Definition:**  
Originally designed for rendering graphics (thousands of pixels simultaneously), GPUs excel at **massively parallel matrix operations** — which is exactly what neural network inference and training requires.

**Why GPUs for AI?**  
Neural network operations = large matrix multiplications (matmul). A 7B parameter model needs billions of multiply-add operations per token. GPUs have thousands of cores that can do these in parallel.

```
Matrix Multiply: A (4096×4096) × B (4096×4096) = C (4096×4096)
  CPU: ~sequential, few cores → SLOW
  GPU: 6,912 CUDA cores doing this in parallel → FAST
```

**GPU Specs for AI:**

| GPU | VRAM | Best For | Approx Cost |
|-----|------|----------|-------------|
| RTX 3060 | 12 GB | 7B models local dev | ~$300 |
| RTX 4090 | 24 GB | 13B models comfortably | ~$1,600 |
| A100 40GB | 40 GB | 30B models fine-tuning | ~$10,000 |
| H100 80GB | 80 GB | 70B models training | ~$30,000 |

---

### ⚡ Key Metrics Comparison

| Metric | CPU | GPU |
|--------|-----|-----|
| Core Count | 4–64 | 1,000–16,000+ |
| Clock Speed | 3–6 GHz | 1–3 GHz |
| Memory Bandwidth | 50–100 GB/s | 900–3,350 GB/s |
| Token Speed (7B) | 5–15 tok/s | 50–150 tok/s |
| Power Usage | 65–253W | 150–700W |
| Memory Type | System RAM | Dedicated VRAM |

---

### 🧮 Why Matrix Math Maps Perfectly to GPUs

```
LLM Inference = Series of Matrix Multiplications

Token embedding → Attention Q×K^T → Softmax → Attention×V → FFN → Output

Each step = matmul over large tensors
GPU's parallel cores = do ALL these multiplications simultaneously
Result = 10–100x speedup over CPU
```

---

### 🌩️ Cloud GPU Options

| Provider | GPU | Use Case |
|----------|-----|----------|
| AWS | A10G, A100, H100 | Enterprise training/inference |
| Google Cloud | TPU v4, A100 | Large-scale training |
| Azure | A100, H100 | Enterprise deployments |
| Lambda Labs | A100, H100 | Cheapest GPU cloud for AI |
| RunPod | RTX 4090, A100 | Cost-effective dev/inference |
| Vast.ai | Various | Cheapest, community GPUs |

---

### 🌍 Real-World Scenario

**Your Agentic RAG on Kubernetes (HealthEdge):**  
Each inference request hits a pod. If CPU-only nodes, expect 10–20 second latency for a complex RAG response — unacceptable for production. Add a GPU node pool (1x T4 on GKE costs ~$0.35/hr), and that same response drops to under 1 second. The Kubernetes resource spec:

```yaml
resources:
  requests:
    memory: "16Gi"
    nvidia.com/gpu: 1
  limits:
    nvidia.com/gpu: 1
```

**Ollama on local machine:**  
- MacBook M2 Pro (16GB unified memory) → ~35 tok/s for Llama 3.2 3B (Apple Silicon GPU)
- Windows machine with RTX 3060 → ~60 tok/s for Llama 3.2 3B
- CPU-only laptop → ~8 tok/s (usable but slow)

---

## 9. Interview Questions

### 🎯 Conceptual Questions

---

**Q1. What is the difference between AI, ML, DL, and GenAI? How do they relate to each other?**

**Answer:**  
They form a nested hierarchy — AI is the broadest field (any machine simulating intelligence), ML is a subset where machines learn from data, DL is a subset of ML using deep neural networks for complex representation learning, and GenAI is a subset of DL focused on generating new content (text, images, audio). Each layer adds specificity and typically requires more data and compute.

---

**Q2. What is a Foundation Model and why is it significant?**

**Answer:**  
A Foundation Model is a large-scale model pre-trained on diverse, massive datasets that can be adapted to many downstream tasks. It's significant because it eliminates the need to train task-specific models from scratch — one pre-trained base (e.g., Llama 3) can be fine-tuned for legal, medical, or coding tasks with a fraction of the compute. Stanford HAI coined the term in 2021, noting their emergent capabilities and broad adaptability.

---

**Q3. Explain the Transformer architecture and why it replaced RNNs.**

**Answer:**  
Transformers use **self-attention mechanisms** to process entire input sequences in parallel, computing relevance scores between all token pairs simultaneously. RNNs process sequentially (each token depends on the previous), making them slow to train and prone to vanishing gradients on long sequences. Transformers: (1) parallelise training dramatically, (2) capture long-range dependencies better via attention, (3) scale more efficiently with data and compute — making them the backbone of all modern LLMs.

---

**Q4. What is RAG and when would you choose it over fine-tuning?**

**Answer:**  
RAG (Retrieval-Augmented Generation) retrieves relevant documents from an external knowledge base at inference time and injects them into the prompt context. Choose RAG when: the knowledge base changes frequently (product catalogue, news, policies), you can't afford fine-tuning compute, or you need source citations/grounding. Choose fine-tuning when: you need the model to adopt a specific style/tone/persona, the task format is very different from base training, or you want the knowledge baked into weights (no retrieval latency).

---

**Q5. What is RLHF and why is it important for LLMs?**

**Answer:**  
RLHF (Reinforcement Learning from Human Feedback) is a training technique where: (1) human raters rank model outputs by quality, (2) a **reward model** is trained on these rankings, (3) the LLM is fine-tuned via PPO (Proximal Policy Optimisation) to maximise reward model scores. It's important because it aligns LLM behaviour with human preferences — making models helpful, harmless, and honest. Without RLHF, a base LLM might produce toxic, biased, or unhelpful content even with perfect language modelling loss.

---

**Q6. What are the three main prompt engineering patterns, and when do you use each?**

**Answer:**  
- **Role-based:** Set a system persona to constrain style, expertise, and tone. Use when you need consistent domain-specific behaviour (legal, medical, technical reviewer).
- **Few-shot:** Provide 2–10 examples of input-output pairs. Use when the task has a specific format (JSON extraction, classification) that examples can demonstrate better than instructions alone.
- **Chain-of-Thought:** Prompt the model to reason step-by-step. Use for complex reasoning, math, multi-step logic where showing intermediate steps dramatically reduces errors.

---

**Q7. What is model quantisation and why does it matter for local LLM deployment?**

**Answer:**  
Quantisation reduces model weight precision — e.g., from 32-bit float (FP32) to 8-bit integer (INT8) or 4-bit (INT4). A 7B parameter model in FP32 requires ~28 GB VRAM; in INT4 (via GGUF format) it fits in ~4 GB. This matters because: (1) enables running large models on consumer hardware (laptops, workstations), (2) reduces inference latency (smaller data = faster memory bandwidth), (3) lowers cost. The trade-off is slight accuracy degradation — usually acceptable for most tasks.

---

**Q8. Explain the difference between temperature, top-k, and top-p sampling in LLM inference.**

**Answer:**  
All three control how the model selects the next token from its probability distribution:
- **Temperature:** Scales the logits before softmax. Low (0.1) = picks highest probability tokens (deterministic, repetitive). High (1.5) = flattens distribution (creative, unpredictable).  
- **Top-K:** Restricts sampling to the K highest probability tokens. K=1 = greedy; K=50 = diverse but coherent.  
- **Top-P (nucleus sampling):** Restricts to the smallest set of tokens whose cumulative probability exceeds P. Top-P=0.9 = adaptively selects tokens; better than top-k for variable vocabulary richness.

---

**Q9. What are the key responsible AI concerns in deploying LLMs in a healthcare context?**

**Answer:**  
- **Privacy:** Patient data (ePHI) must not leave the organisation — mandates local/on-premise LLMs or a HIPAA BAA with cloud providers.
- **Hallucination:** LLMs can fabricate medical information — RAG with grounded medical knowledge bases + human-in-the-loop for clinical decisions is essential.
- **Bias:** Models trained on Western medical literature may perform poorly for Indian patient populations, diseases, or drug names.
- **Explainability:** Clinical decisions need justification (why did the model flag this? which source?).
- **Accountability:** Human clinicians remain legally accountable — AI is decision support, not decision maker.

---

**Q10. When would you choose a local LLM (Ollama) over an API-based LLM (OpenAI/Claude), and what are the infrastructure trade-offs?**

**Answer:**  
Choose local when: data is sensitive (PII, PHI, trade secrets), offline operation is required, cost at scale is prohibitive, or you need full customisation (quantise, fine-tune, modify system). Choose API when: you need SOTA quality, have bursty/unpredictable load, want zero infra management, or are in prototyping phase.  
Infrastructure trade-offs: Local requires GPU hardware, memory management, model versioning, and inference optimisation (batching, quantisation). API abstracts all this but introduces network latency, data privacy concerns, per-token cost, and vendor lock-in. In production (your Kubernetes setup), a hybrid is common — sensitive workloads on local, best-quality tasks on API.

---

**Q11. What is the attention mechanism in Transformers and what problem does it solve?**

**Answer:**  
Attention computes a weighted sum of all values (V) in the sequence, where weights are determined by the similarity between query (Q) and keys (K):  
`Attention(Q,K,V) = softmax(QK^T / √d_k) × V`  
It solves the **long-range dependency problem** of RNNs — in an RNN, information from early tokens gets diluted over many steps. Attention allows any token to directly attend to any other token in one step, regardless of distance. Multi-head attention does this with multiple learned Q/K/V projection matrices simultaneously, capturing different relationship types (syntactic, semantic, positional).

---

**Q12. What is the difference between encoder-only, decoder-only, and encoder-decoder Transformer architectures?**

**Answer:**  
- **Encoder-only (BERT):** Reads full input bidirectionally. Best for understanding tasks — classification, NER, semantic similarity. Not designed for generation.
- **Decoder-only (GPT family, Llama):** Auto-regressive — generates one token at a time, attending only to previous tokens (causal masking). Best for generation tasks. Most modern LLMs use this.
- **Encoder-Decoder (T5, BART, original Transformer):** Encoder processes input, decoder generates output. Best for seq2seq tasks — translation, summarisation, question answering with long contexts.

---

*📝 Notes compiled for the GenAI Developer Track — Module: Introduction to Generative AI*  
*Last updated: June 2026*
