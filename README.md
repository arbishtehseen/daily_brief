# 📰 Daily Brief (Smart News Digest & AI Summarizer)

An automated backend pipeline that scrapes daily news headlines from [Dawn News](https://www.dawn.com), processes and cleans them, generates structured **bilingual summaries (English & Urdu)** using Groq AI, and delivers them directly to your inbox via secure Gmail SMTP. Built with a robust, modular software engineering architecture and automated via a background scheduler.

---

## 🛠️ Project Architecture & Modular Design

The project follows a clean separation-of-concerns design pattern:

```text
daily_brief/
│
├── scrapper.py       # Handles HTTP requests, robust error handling, and DOM parsing
├── summarizer.py     # Interfaces with Groq API, formats prompts, and splits bilingual text
├── notifier.py       # Manages secure MIME multipart email delivery via Gmail SMTP
├── helpers.py        # Contains utility functions for filtering, cleaning, and deduplication
├── scheduler.py      # Runs non-blocking background execution loops using the schedule library
├── main.py           # Core orchestrator tying the entire pipeline together
├── requirements.txt  # Project dependencies
└── .env              # Environment credentials (Git-ignored for security)

⚙️ Tech Stack & Dependencies
Language: Python 3.10+

Web Scraping: requests, BeautifulSoup4

AI & LLM Integration: groq (leveraging high-speed LLMs for structured summarization)

Email Automation: Python built-in smtplib, email.mime

Text Processing & Bidi: arabic-reshaper, python-bidi (for proper Urdu rendering)

Automation: schedule

🚀 Key Features
Robust Error Handling: Built-in connection timeouts, invalid URL checks, and graceful exception handling for network instabilities.

Structured Bilingual LLM Prompting: Enforces strict formatting guidelines to output clean bullet points grouped by topic in both English and Urdu.

Secure Credential Management: Utilizes environment variables (python-dotenv) and Gmail App Passwords to secure SMTP transmissions.

Automation Ready: Configured with a non-blocking scheduler loop to execute daily briefs reliably.

Installation & Setup
1. Clone the Repository
Bash
git clone [https://github.com/arbishtehseen/daily_brief.git](https://github.com/arbishtehseen/daily_brief.git)
cd daily_brief
2. Create and Activate Virtual Environment
Bash
python -m venv venv
# On Windows (PowerShell):
.\venv\Scripts\Activate
# On macOS/Linux:
source venv/bin/activate
3. Install Dependencies
Bash
pip install -r requirements.txt
4. Configure Environment Variables
Create a .env file in the root directory and add your credentials:

Code snippet
GROQ_API_KEY=your_groq_api_key_here
SENDER_EMAIL=your_email@gmail.com
SENDER_PASSWORD=your_gmail_app_password_here
RECEIVER_EMAIL=recipient_email@gmail.com
💻 Usage
Run Manually (One-time Pipeline Execution):
Bash
python main.py
Run Automated Background Scheduler:
Bash
python scheduler.py
