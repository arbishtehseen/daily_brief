import time

import schedule

from main import run_daily_brief

RUN_TIME = "09:00"  

def safe_run():
    try:
        run_daily_brief()
    except Exception as e:
        print(f"Run failed: {e}")


schedule.every().day.at(RUN_TIME).do(safe_run)
print(f"Scheduler started. DailyBrief will run every day at {RUN_TIME}.")

while True:
    schedule.run_pending()
    time.sleep(60)