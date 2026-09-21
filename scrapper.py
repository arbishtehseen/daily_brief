import requests
from bs4 import BeautifulSoup
url = "https://www.dawn.com"

def verify_access(url): 
    try:
        headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout = 10)
        if (response.status_code == 200):
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
    except requests.exceptions.InvalidURL : 
        print("Invalid URL")
        return None
    except Exception as e:
        print(f"Unexpected Error : {e}")
        return None
    
response = verify_access(url)

def parse_html(response):
    if response is None:
        print("Couldn't get website's access")
        return None
    else:
        soup = BeautifulSoup(response.text , "html.parser")
        return soup

Soup = parse_html(response)

def get_headlines(soup):
    headline_tags = soup.find_all("h2", class_="story__title")
    headlines = []
    for tag in headline_tags:
        text = tag.text.strip()
        headlines.append(text)
    return headlines


headlines = get_headlines(Soup)
print(headlines)


