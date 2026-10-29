import os
from notifier import send_email
from dotenv import load_dotenv
from groq import Groq

import arabic_reshaper
from bidi.algorithm import get_display

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

def create_prompt(headlines_list):
    headlines_text = "\n".join(headlines_list)
    prompt = f"""Act as a professional editor with 10 years of experience in documentation and content summarization. You will be given a list of news headlines. Your task is to:
1. Combine and group all related or overlapping topics together.
2. Summarize them into clear, concise bullet points using professional wording — do not add any extra details, opinions, or information beyond what is provided.
3. Present this summary in English first.
4. Then, translate the same bullet-point summary into Urdu, maintaining the same structure and professional tone.

Format your response exactly as follows:
ENGLISH:
[English bullet points here]

URDU:
[Urdu bullet points here]

Headlines:
{headlines_text}
"""
    return prompt

def get_ai_summary(prompt):
    try:
        response = client.chat.completions.create(
            model="qwen/qwen3.8-27b",  
            messages=[{"role": "user", "content": prompt}],
            max_tokens=800
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"couldn't get summary from AI. Error: {e}")
        return None

def split_summary(full_summary):
    if not full_summary: 
        return None, None
    
    if "URDU:" in full_summary:
        parts = full_summary.split("URDU:")
        english_part = parts[0].replace("ENGLISH:", "").strip()
        urdu_part = parts[1].strip()
    else:
        english_part = full_summary.replace("ENGLISH:", "").strip()
        urdu_part = "URDU Summary ain't available"
        
    return english_part, urdu_part

def summarize_headlines(headlines_list):
    if not headlines_list:
        print("No headlines found from scraper. Skipping AI call.")
        return "No headlines scraped", "کوئی سرخی نہیں ملی"
    
    prompt = create_prompt(headlines_list)
    full_summary = get_ai_summary(prompt)
    
    if not full_summary:
        return "Failed to generate summary", "خلاصہ حاصل کرنے میں ناکامی"
        
    english_summary, urdu_summary = split_summary(full_summary)
    return english_summary, urdu_summary

if __name__ == "__main__":
    from scrapper import scrape_news
    
    url = "https://www.dawn.com"
    headlines = scrape_news(url)
    
    english, urdu = summarize_headlines(headlines)
    
    print("\n--- ENGLISH SUMMARY ---")
    print(english)
    
    print("\n--- URDU SUMMARY ---")
    # Urdu reshaping and bidi processing for proper terminal output
    reshaped_text = arabic_reshaper.reshape(urdu)
    bidi_text = get_display(reshaped_text)
    print(bidi_text)
    
    # --- Email Notification Integration ---
    email_content = f"--- ENGLISH SUMMARY ---\n{english}\n\n--- URDU SUMMARY ---\n{urdu}"
    send_email(email_content)