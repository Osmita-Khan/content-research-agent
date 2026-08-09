"""
AI Content Research & Brief Generator
---------------------------------------
Automates the research phase of content writing: give it a topic,
it searches for current information, then uses AI to turn that
research into a structured content brief (hook, key stats, target
audience, and a suggested outline).

Author: Osmita Khan

HOW TO RUN THIS (no coding experience needed):
1. Open a terminal in this folder.
2. Install the two required libraries (one-time setup):
     pip install google-generativeai tavily-python
3. Paste your two free API keys into the placeholders below,
   in the CONFIGURATION section.
4. Run the script:
     python agent.py
5. When prompted, type a topic and press Enter.
"""

import google.generativeai as genai
from tavily import TavilyClient

# =========================================================
# CONFIGURATION — paste your free API keys between the quotes
# =========================================================
GEMINI_API_KEY = "PASTE_YOUR_GEMINI_API_KEY_HERE"   # from aistudio.google.com
TAVILY_API_KEY = "PASTE_YOUR_TAVILY_API_KEY_HERE"    # from tavily.com

# =========================================================
# SETUP — connects to both services using the keys above
# =========================================================
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")
search_client = TavilyClient(api_key=TAVILY_API_KEY)


def research_topic(topic, max_results=5):
    """
    Step 1: Search the web for current, relevant information on the topic.
    Returns a list of search results (title, url, and a short snippet each).
    """
    print(f"\nSearching for recent information on: {topic} ...")
    results = search_client.search(
        query=topic,
        search_depth="advanced",
        max_results=max_results
    )
    return results.get("results", [])


def build_research_summary(search_results):
    """
    Step 2: Turn the raw search results into a single block of text
    that we can hand to the AI model. Each source is numbered so the
    brief can reference where each stat or claim came from.
    """
    summary_lines = []
    for i, result in enumerate(search_results, start=1):
        title = result.get("title", "Untitled source")
        url = result.get("url", "")
        snippet = result.get("content", "")[:500]  # keep each snippet short
        summary_lines.append(f"[Source {i}] {title} ({url})\n{snippet}\n")
    return "\n".join(summary_lines)


def generate_content_brief(topic, research_summary):
    """
    Step 3: Send the topic and research summary to Gemini, and ask it
    to produce a structured content brief: hook, key stats, audience,
    and a suggested outline. This is the same brief a content writer
    would normally build by hand before starting to write.
    """
    prompt = f"""
You are a content strategist preparing a research brief for a writer.

Topic: {topic}

Below is recent research gathered on this topic, with numbered sources:

{research_summary}

Using only the information above, produce a content brief with these
exact sections:

1. HOOK — one sentence that could open the article or post.
2. KEY STATS & FACTS — 3 to 5 bullet points, each citing which source
   number it came from, e.g. "(Source 2)".
3. TARGET AUDIENCE — who would care about this and why, in 1-2 sentences.
4. SUGGESTED OUTLINE — a short outline with an intro, 2-3 body
   sections, and a closing point.

Keep the tone practical and specific. Do not invent statistics that
are not in the research above.
"""
    response = model.generate_content(prompt)
    return response.text


def main():
    print("=" * 55)
    print("AI CONTENT RESEARCH & BRIEF GENERATOR")
    print("=" * 55)

    topic = input("\nEnter a content topic (e.g. 'MFS growth in Bangladesh'): ").strip()

    if not topic:
        print("No topic entered. Exiting.")
        return

    # Step 1: search
    search_results = research_topic(topic)

    if not search_results:
        print("No search results found. Try a different or broader topic.")
        return

    # Step 2: summarize search results into one text block
    research_summary = build_research_summary(search_results)

    # Step 3: generate the structured brief
    print("Generating content brief...\n")
    brief = generate_content_brief(topic, research_summary)

    # Step 4: show the result
    print("=" * 55)
    print("CONTENT BRIEF")
    print("=" * 55)
    print(brief)

    # Also save it to a text file so it's not lost
    filename = "content_brief_output.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"Topic: {topic}\n\n{brief}")
    print(f"\nBrief also saved to: {filename}")


if __name__ == "__main__":
    main()
