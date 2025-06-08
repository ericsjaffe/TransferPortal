import requests
from bs4 import BeautifulSoup

def get_ranking_data():
    url = "https://www.on3.com/transfer-portal/rankings/football/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    updates = []
    rows = soup.select("tr")

    for row in rows[1:]:
        cols = row.find_all("td")
        if len(cols) < 8:
            continue

        try:
            rank = cols[0].get_text(strip=True)
            name = cols[1].get_text(strip=True)
            position = cols[2].get_text(strip=True)
            rating = cols[3].get_text(strip=True)
            nil_value = cols[4].get_text(strip=True)
            status = cols[5].get_text(strip=True)
            last_team = cols[6].get_text(strip=True)
            new_team = cols[7].get_text(strip=True)

            updates.append({
                "rank": rank,
                "name": name,
                "position": position,
                "rating": rating,
                "nil_value": nil_value,
                "status": status,
                "last_team": last_team,
                "new_team": new_team
            })
        except:
            continue

        if len(updates) >= 25:
            break

    return updates
