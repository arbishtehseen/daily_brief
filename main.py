from scrapper import scrape_news
from summarizer import summarize_headlines
from notifier import send_email
from database import init_db, is_headline_sent, save_headline

def run_daily_brief():
    print("Starting DailyBrief...")
    
    init_db()

    URL = "https://www.dawn.com"
    
    headlines = scrape_news(URL)
    if not headlines:
        print("No headlines scraped. Stopping execution.")
        return False
    new_headlines = []
    for h in headlines:
        if not is_headline_sent(h):
            new_headlines.append(h)
            save_headline(h)

    if not new_headlines:
        print("No new headlines found! All headlines have already been sent. Stopping.")
        return False

    print(f"Total {len(new_headlines)} new headlines found. Processing summaries...")

 
    english, urdu = summarize_headlines(new_headlines)
    if not english or not urdu:
        print("Summary generation failed. Stopping, no email sent.")
        return False

    success = send_email(english, urdu)
    if success:
        print("Daily Brief workflow completed successfully!")
    
    return success

if __name__ == "__main__":
    run_daily_brief()
