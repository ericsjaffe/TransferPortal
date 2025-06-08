import requests
from bs4 import BeautifulSoup

def get_football_transfer_updates():
    url = "https://www.on3.com/transfer-portal/wire/football/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    updates = []
    articles = soup.select("article")

    for article in articles:
        title_tag = article.select_one("h3")
        link_tag = article.find("a", href=True)
        img_tag = article.find("img")
        time_tag = article.select_one("time")

        if not title_tag or not link_tag:
            continue

        title = title_tag.get_text(strip=True)
        link = link_tag["href"]
        if link.startswith("/"):
            link = "https://www.on3.com" + link
        image = img_tag["src"] if img_tag and img_tag.get("src") else None
        time = time_tag.get_text(strip=True) if time_tag else "Recently"

        updates.append({
            "title": title,
            "link": link,
            "image": image,
            "time": time
        })

        if len(updates) >= 20:
            break

    return updates
