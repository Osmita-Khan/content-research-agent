# AI Content Research & Brief Generator

An automation tool that replicates the research-to-brief workflow used to produce 300+ published articles and social media posts on financial topics. Give it a topic, and it searches for current information, then uses AI to turn that research into a structured content brief ready for writing.

## Why I built this

Before writing content on financial products, market trends, or policy developments, the research phase (finding relevant data, checking recent news, figuring out an audience angle) often takes as long as the writing itself. This tool automates that first step, producing a structured brief with a suggested hook, key stats, target audience framing, and an outline.

## How it works

1. **Input** — you provide a topic (e.g. "MFS growth in Bangladesh").
2. **Search** — the tool searches the web for current, relevant sources using the Tavily Search API.
3. **Synthesize** — the search results are compiled into a research summary with numbered sources.
4. **Generate** — Google's Gemini model reads the research and produces a structured content brief: a hook, 3-5 key stats (each cited to its source), the target audience, and a suggested outline.
5. **Output** — the brief prints to the screen and saves to a text file.

## Tech stack

- Python
- Google Gemini API (free tier) — for AI-generated analysis
- Tavily Search API (free tier) — for real-time web research

## Setup

### 1. Install dependencies
```bash
pip install google-generativeai tavily-python
```

### 2. Get your free API keys
- **Gemini API key**: [aistudio.google.com](https://aistudio.google.com) → "Get API key" (no card required)
- **Tavily API key**: [tavily.com](https://tavily.com) → sign up, key is shown on your dashboard (no card required)

### 3. Add your keys
Open `agent.py` and paste your keys into the configuration section near the top:
```python
GEMINI_API_KEY = "your-key-here"
TAVILY_API_KEY = "your-key-here"
```

### 4. Run it
```bash
python agent.py
```
You'll be prompted to enter a topic. The brief will print to your screen and also save as `content_brief_output.txt`.

## Sample output

```
Topic: MFS growth in Bangladesh

1. HOOK
Bangladesh's mobile financial services market has grown fast enough
that rural adoption now outpaces urban adoption for the first time.

2. KEY STATS & FACTS
- MFS transaction volume grew significantly year-over-year (Source 1)
- Agent banking network expansion has been a key growth driver (Source 2)
- Regulatory changes have shaped recent market dynamics (Source 3)

3. TARGET AUDIENCE
Fintech professionals and policy stakeholders interested in financial
inclusion trends in South Asia.

4. SUGGESTED OUTLINE
- Intro: framing the growth trend
- Body 1: what's driving adoption
- Body 2: regulatory context
- Close: what this signals for the sector
```

## Process flow

See `flowchart.png` for a visual diagram of the full pipeline: topic input → web search → research synthesis → AI brief generation → output.

## Author

Osmita Khan — Finance student, Institute of Business Administration, University of Dhaka
