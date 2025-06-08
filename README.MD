# PortalDecision - NCAA Football Transfer Portal Top 200

## How to Use

1. **Scrape the latest player data:**
    ```
    python scrape_on3.py
    ```
    This creates `static_data.json` in the project folder.

2. **Run the web app locally:**
    ```
    flask run
    ```
    or
    ```
    python app.py
    ```

3. **Deploy to Render:**
    - Push all files to a GitHub repo.
    - Create a new Render "Web Service" and connect your repo.
    - Set the Start Command:  
      ```
      gunicorn app:app
      ```
    - (Optional) Add a Render Job for regular scraping updates.

## Requirements
- Python 3.9+
- Flask, Selenium, webdriver-manager

## Notes
- Make sure to run `scrape_on3.py` periodically to update data.
- Team logos are mapped for Power 5 teams; add others as needed in `scrape_on3.py`.

