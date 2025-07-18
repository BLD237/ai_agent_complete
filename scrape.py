import requests
from bs4 import BeautifulSoup
from readability import Document

def scrape_google(query):
    headers = {"User-Agent": "Mozilla/5.0"}
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    
    results = []
    for g in soup.select("div.g")[:3]:
        title = g.select_one("h3")
        link_tag = g.select_one("a")
        if title and link_tag:
            link = link_tag["href"]
            results.append(f"[{title.text}]({link})")
    return "\n".join(results)


def scrape_main_content(url):
    """
    Fetches the main content from a web page, cleans it, and returns the readable text.
    """
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    response.raise_for_status()
    doc = Document(response.text)
    html = doc.summary()
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text(separator="\n", strip=True)
    return text
