from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

def get_ranking_data():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    url = "https://www.on3.com/transfer-portal/rankings/football/"
    driver.get(url)
    time.sleep(6)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    updates = []
    rows = soup.select("tbody tr")

    for row in rows:
        cols = row.find_all("td")
        if len(cols) < 8:
            continue

        updates.append({
            "rank": cols[0].text.strip(),
            "name": cols[1].text.strip(),
            "position": cols[2].text.strip(),
            "rating": cols[3].text.strip(),
            "nil_value": cols[4].text.strip(),
            "status": cols[5].text.strip(),
            "last_team": cols[6].text.strip(),
            "new_team": cols[7].text.strip()
        })

        if len(updates) >= 25:
            break

    return updates
