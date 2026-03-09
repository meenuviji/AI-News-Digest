# src/digest.py
from groq import Groq
from datetime import datetime


def generate_digest(articles_by_category, api_key):
    """Use Groq (Llama 3.3) to curate and summarize articles into an HTML digest."""
    client = Groq(api_key=api_key)
    today  = datetime.now().strftime("%A, %B %d, %Y")

    article_text = _format_articles(articles_by_category)

    prompt = f"""You are an expert AI journalist and editor. Today is {today}.

Below are raw RSS feed articles collected in the last 24 hours about AI.
Produce a daily AI digest email in clean HTML.

RULES:
1. Select only the 3-5 MOST significant/innovative articles per category.
2. Skip duplicates, fluff, or low-value content.
3. For each selected article, write a 2-3 sentence insight explaining WHY it matters.
4. Add a "🔥 Top Story of the Day" section at the very top.
5. End with a "💡 Key Takeaway" paragraph summarizing today's overall AI theme.

OUTPUT FORMAT:
- Return ONLY a valid HTML body fragment
- No html, head, or body tags
- Inline CSS only, no style blocks
- Primary color: deep purple (#6B21A8)
- White background, clean modern design
- Max-width 680px, mobile-friendly
- Article titles must be clickable links
- Source shown as a small colored badge

ARTICLES:
{article_text}"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=4000,
    )
    return response.choices[0].message.content


def _format_articles(articles_by_category):
    """Format articles into a readable text block for the prompt."""
    text = ""
    for category, articles in articles_by_category.items():
        text += f"\n\n### {category}\n"
        for a in articles:
            text += (
                f"- [{a['source']}] {a['title']}\n"
                f"  URL: {a['link']}\n"
                f"  Published: {a['published']}\n"
                f"  Summary: {a['summary']}\n\n"
            )
    return text