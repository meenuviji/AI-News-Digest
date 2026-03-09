# main.py
import os
import sys
import logging
from datetime import datetime
from dotenv import load_dotenv

from src.fetcher import fetch_articles
from src.digest  import generate_digest
from src.emailer import send_digest

# ── Logging: prints to screen AND saves to logs/ folder ───
os.makedirs("logs", exist_ok=True)
log_file = f"logs/digest_{datetime.now().strftime('%Y%m%d')}.log"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)s  %(message)s",
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler(sys.stdout),
    ]
)
log = logging.getLogger(__name__)

# ── Load secrets from .env file ────────────────────────────
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
SENDER_EMAIL    = os.getenv("SENDER_EMAIL", "")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD", "")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL", "")
HOURS_LOOKBACK  = int(os.getenv("HOURS_LOOKBACK", "24"))
MAX_ARTICLES    = int(os.getenv("MAX_ARTICLES", "30"))


def validate_config():
    """Make sure all required environment variables are set."""
    missing = [k for k, v in {
        "GROQ_API_KEY": GROQ_API_KEY,
        "SENDER_EMAIL":    SENDER_EMAIL,
        "SENDER_PASSWORD": SENDER_PASSWORD,
        "RECIPIENT_EMAIL": RECIPIENT_EMAIL,
    }.items() if not v]

    if missing:
        log.error(f"Missing environment variables: {', '.join(missing)}")
        log.error("Copy .env.example → .env and fill in your values.")
        sys.exit(1)


def main():
    log.info("══════════════════════════════════════════════════")
    log.info("   AI Daily News Digest — Starting Run")
    log.info("══════════════════════════════════════════════════")

    validate_config()

    log.info(f"Fetching articles from the last {HOURS_LOOKBACK} hours...")
    articles = fetch_articles(
        hours_lookback=HOURS_LOOKBACK,
        max_per_category=MAX_ARTICLES // 4 if MAX_ARTICLES >= 4 else 4
    )

    total = sum(len(v) for v in articles.values())
    if total == 0:
        log.warning("No articles found. Try increasing HOURS_LOOKBACK in .env.")
        sys.exit(0)

    log.info(f"Found {total} articles across {len(articles)} categories.")
    log.info("Generating digest with Gemini...")

    html_body = generate_digest(articles, GROQ_API_KEY)

    log.info("Sending email...")
    send_digest(html_body, SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL)

    log.info(f"✅ Digest delivered to {RECIPIENT_EMAIL}")
    log.info("Run complete.\n")


if __name__ == "__main__":
    main()