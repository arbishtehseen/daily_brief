from scrapper import scrape_news
from summarizer import summarize_headlines
from notifier import send_email

URL = "https://www.dawn.com"

# runs the whole pipeline: scrape -> summarize -> email
def run_daily_brief():
    print("Starting DailyBrief...")

    # step 1: scrape
    headlines = scrape_news(URL)
    if not headlines:
        print("No headlines scraped. Stopping.")
        return False

    # step 2: summarize (English + Urdu)
    english, urdu = summarize_headlines(headlines)
    if not english or not urdu:
        print("Summary failed. Stopping, no email sent.")
        return False

    # step 3: combine content and send email (matching notifier.py's single argument)
    email_content = f"--- ENGLISH SUMMARY ---\n{english}\n\n--- URDU SUMMARY ---\n{urdu}"
    return send_email(email_content)

if __name__ == "__main__":
    run_daily_brief()