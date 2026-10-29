# 📰  Daily Brief — Automated News Intelligence Pipeline

A production-grade, stateful backend pipeline built in Python that automatically ingests live news headlines, generates bilingual summaries using Groq LLM API, manages local state persistence to prevent duplicate content, and delivers structured HTML email briefings.

---

## 🎯 Key Features

- **Automated Data Ingestion:** Scrapes real-time headline data and metadata using BeautifulSoup4.
- **LLM-Powered Summarization:** Leverages the Groq API (Llama-3) for bilingual intelligence synthesis (English & Urdu).
- **State Persistence & Deduplication:** Integrates an SQLite database layer to track processed articles, avoiding duplicate emails and unnecessary API execution.
- **Responsive Email Delivery:** Dispatches styled HTML/CSS email templates with custom typography and native Right-to-Left (`RTL`) text layout support for Urdu content.
- **Modular Architecture:** Structured with strict separation of concerns across scraping, processing, storage, and notification modules.

---

## 🛠️ System Architecture & Tech Stack

- **Language:** Python 3.x
- **Scraping Engine:** `beautifulsoup4`, `requests`
- **AI Processing:** `groq` SDK
- **Database Layer:** SQLite3
- **Notification Engine:** `smtplib`, `email.mime`
- **Environment Management:** `python-dotenv`

---

## 📁 Repository Structure

```text
├── database.py       # SQLite connection, schema initialization, and state tracking
├── main.py           # Pipeline orchestrator and main execution flow
├── notifier.py       # Email formatting, HTML/CSS layout rendering, and SMTP delivery
├── scrapper.py       # Web scraping logic for news extraction
├── summarizer.py     # Groq API integration for bilingual summarization
├── requirements.txt  # Project dependencies
└── README.md         # Project documentation

⚙️ Setup & Installation
1. Clone the Repository
Bash
git clone [https://github.com/arbishtehseen/daily_brief.git](https://github.com/arbishtehseen/daily_brief.git)
cd daily_brief
2. Set Up Virtual Environment
Bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
3. Install Dependencies
Bash
pip install -r requirements.txt
4. Configure Environment Variables
Create a .env file in the root directory and specify the following keys:

Code snippet
GROQ_API_KEY=your_groq_api_key_here
SENDER_EMAIL=your_gmail_address@gmail.com
SENDER_PASSWORD=your_app_passcode_here
RECEIVER_EMAIL=recipient_email@gmail.com
🚀 Execution
Run the main orchestration script:

Bash
python main.py
🔒 Security & Privacy Notice
Sensitive credentials and database binaries (.env, *.db) are strictly excluded from version control via .gitignore.

Password authentication uses Gmail App Passwords over TLS encryption via SMTP.
