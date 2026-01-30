# Paper-to-Podcast 🎤

**Paper-to-Podcast** turns academic research papers into an engaging, three-person podcast conversation. Instead of a flat text‑to‑speech readout, it generates a structured discussion between distinct personas so listeners can absorb complex material **hands‑free** (e.g., during commutes or workouts).

---

## Objective

The goal is to make dense research **accessible and enjoyable** by simulating a natural conversation around the paper:

- Distills key sections into plain language
- Surfaces intuitive questions and clarifications
- Adds expert context and critical thinking
- Delivers the result as a multi‑speaker audio track

---

## Personas

- **Host** – Guides the episode, introduces sections, and keeps the tone warm and engaging.  
- **Learner** – Asks intuitive questions and expresses confusion to surface explanations.  
- **Expert** – Provides deeper technical insight, connections, and implications.

This persona design creates a more “human” listening experience than a single‑voice summary.

---

## Architecture & Key Components

- **Planning Chain**  
  Builds a section‑by‑section outline of the conversation from the paper. This keeps the model on track and reduces hallucinations and repetition.

- **Discussion Chain (RAG)**  
  Uses **retrieval‑augmented generation** to ground each segment in the original paper, expanding the outline into a detailed, persona‑driven script.

- **Enhancement Chain**  
  Cleans up redundancies, smooths transitions, and enforces a coherent, episode‑like flow.

- **Text-to-Speech**  
  Uses the **OpenAI API** to turn the final script into audio, assigning different voices to each persona for a true multi‑speaker effect.

---

## Cost Efficiency

The pipeline is optimized for low inference cost.  
Example: generating a ~9‑minute podcast from a 19‑page paper costs **≈$0.16** with the current OpenAI configuration.

---

## Getting Started

### Prerequisites

- Python 3.8+  
- OpenAI API key (stored in `.env` as `OPENAI_API_KEY`)  
- Streamlit for the UI

### Run the App

```bash
streamlit run app.py
