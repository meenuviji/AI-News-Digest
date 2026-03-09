# 🤖 AI Daily News Digest

> An automated daily email digest of the most important AI news —
> curated and summarized by AI, delivered to your inbox every morning.

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square&logo=python)
![Groq](https://img.shields.io/badge/Powered%20by-Groq%20AI-orange?style=flat-square)
![Gemini](https://img.shields.io/badge/Powered%20by-Gemini%20AI-blue?style=flat-square&logo=google)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

---

## ✨ What It Does

Every day at a scheduled time, this autonomous agent:

1. 📡 **Fetches** the latest articles from 16 top AI/tech RSS feeds
2. 🤖 **Curates** using LLM — selects only the most significant stories and writes real insights
3. 📧 **Delivers** a beautiful HTML digest to your inbox — zero action required

---

## 📬 Digest Sections

| Section | Description |
|---|---|
| 🔥 Top Story of the Day | The single biggest AI story of the day |
| 🛠 New AI Tools & Apps | Latest product launches and tools |
| 🧠 LLMs & Model Releases | New model drops and updates |
| 🏥 AI in Industry | Real-world applications across sectors |
| 🔬 Research Breakthroughs | Notable papers and academic advances |
| 💡 Key Takeaway | Daily theme summary |

---

## 🗂 Project Structure
```
ai-news-digest/
│
├── main.py              # Entry point — orchestrates the full pipeline
│
├── src/
│   ├── fetcher.py       # RSS feed fetching and parsing
│   ├── digest.py        # LLM summarization and HTML generation
│   └── emailer.py       # Gmail SMTP delivery
│
├── config/
│   └── feeds.py         # All RSS feed sources — easy to customize
│
├── logs/                # Auto-generated daily run logs
├── requirements.txt     # Python dependencies
└── .env.example         # Environment variables template
```

---

## 📡 News Sources

**New AI Tools & Apps**
TechCrunch AI · The Verge AI · VentureBeat AI · Product Hunt

**LLMs & Model Releases**
Hugging Face Blog · OpenAI Blog · Google DeepMind · Mistral AI

**AI in Industry**
MIT Technology Review · Wired AI · Forbes AI · ZDNet AI

**Research Breakthroughs**
ArXiv CS.AI · ArXiv CS.LG · Papers With Code · Google AI Blog

---

## 🚀 Setup

### 1. Clone the repo
```bash
git clone https://github.com/meenuviji/AI-News-Digest.git
cd AI-News-Digest
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure credentials
```bash
cp .env.example .env
```

Edit `.env` with your API key and Gmail App Password:
```env
GROQ_API_KEY=your-groq-api-key
SENDER_EMAIL=youremail@gmail.com
SENDER_PASSWORD=your-gmail-app-password
RECIPIENT_EMAIL=youremail@gmail.com
MAX_ARTICLES=16
HOURS_LOOKBACK=48
```

### 4. Run manually
```bash
python3 main.py
```

### 5. Schedule daily (Mac/Linux)
```bash
crontab -e
# Add this line to run every day at 7 AM:
0 7 * * * /usr/bin/python3 /full/path/to/main.py
```

---

## 🛠 Tech Stack

| Tool | Purpose |
|---|---|
| **Python 3.9+** | Core language |
| **Groq (Llama 3.3 70B)** | AI summarization — free tier |
| **Google Gemini** | Alternative AI backend |
| **feedparser** | RSS feed parsing |
| **smtplib** | Email delivery via Gmail |
| **python-dotenv** | Secure credential management |

---

## 🔒 Security

- All credentials stored in `.env` — never committed to GitHub
- `.gitignore` explicitly blocks `.env` and log files
- Gmail App Password used instead of real account password

---

## 🗺 Roadmap

- [ ] Switch to Gemini API as primary LLM
- [ ] Add cron job for full automation
- [ ] Weekly trend tracker
- [ ] Streamlit dashboard for browsing past digests
- [ ] Multi-subscriber support

---

## 👩‍💻 Author

**Meena Periasamy**
M.S. Data Analytics Engineering · Northeastern University

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/meenuviji/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=flat-square&logo=github)](https://github.com/meenuviji)

---

*Built with Python · Powered by Groq + Gemini AI · Delivered via Gmail*
