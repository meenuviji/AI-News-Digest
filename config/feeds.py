# config/feeds.py
# Add or remove RSS feeds here anytime — no other file needs to change

RSS_FEEDS = {
    "New AI Tools & Apps": [
        ("TechCrunch AI",     "https://techcrunch.com/category/artificial-intelligence/feed/"),
        ("The Verge AI",      "https://www.theverge.com/ai-artificial-intelligence/rss/index.xml"),
        ("VentureBeat AI",    "https://venturebeat.com/category/ai/feed/"),
        ("Product Hunt",      "https://www.producthunt.com/feed"),
    ],
    "LLMs & Model Releases": [
        ("Hugging Face Blog", "https://huggingface.co/blog/feed.xml"),
        ("OpenAI Blog",       "https://openai.com/blog/rss/"),
        ("Google DeepMind",   "https://deepmind.google/blog/rss/"),
        ("Mistral AI",        "https://mistral.ai/news/rss"),
    ],
    "AI in Industry": [
        ("MIT Tech Review",   "https://www.technologyreview.com/topic/artificial-intelligence/feed"),
        ("Wired AI",          "https://www.wired.com/feed/tag/ai/latest/rss"),
        ("Forbes AI",         "https://www.forbes.com/ai/feed/"),
        ("ZDNet AI",          "https://www.zdnet.com/topic/artificial-intelligence/rss.xml"),
    ],
    "Research Breakthroughs": [
        ("ArXiv CS.AI",       "https://rss.arxiv.org/rss/cs.AI"),
        ("ArXiv CS.LG",       "https://rss.arxiv.org/rss/cs.LG"),
        ("Papers With Code",  "https://paperswithcode.com/latest.rss"),
        ("Google AI Blog",    "https://blog.research.google/feeds/posts/default"),
    ],
}