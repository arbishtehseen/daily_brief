import requests
from bs4 import BeautifulSoup
from helpers import filter_headlines, remove_duplicates, limit_headlines

url = "https://www.dawn.com"

def verify_access(url): 
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            return response  
        else: 
            print(f"Website not found, Status {response.status_code}")
            return None
    except requests.exceptions.ConnectionError:
        print("No internet connection.")
        return None
    except requests.exceptions.Timeout:
        print("Website is taking too long to respond!")
        return None
    except requests.exceptions.InvalidURL: 
        print("Invalid URL")
        return None
    except Exception as e:
        print(f"Unexpected Error : {e}")
        return None

def parse_html(response):
    if response is None:
        print("Couldn't get website's access")
        return None
    else:
        soup = BeautifulSoup(response.text, "html.parser")
        return soup


def get_headlines(soup):
    if soup is None:
        return []
    headline_tags = soup.find_all("h2", class_="story__title")
    headlines = []
    for tag in headline_tags:
        text = tag.text.strip()
        headlines.append(text)
    return headlines


def scrape_news(url):
    response = verify_access(url)
    if response is None:
        return []
    else: 
        soup = parse_html(response)
        headlines = get_headlines(soup)
        headlines_list = filter_headlines(headlines)
        headlines_list = remove_duplicates(headlines_list)
        final_headlines_list = limit_headlines(headlines_list)
        return final_headlines_list

if __name__ == "__main__":
 
    test_headlines = scrape_news(url)
    print(f"Successfully scraped {len(test_headlines)} headlines!")
    for h in test_headlines[:5]:
        print(f"- {h}")