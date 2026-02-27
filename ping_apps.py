from playwright.sync_api import sync_playwright
import time

urls = [
    'https://bio-concepts-simplifiedv2-yash.streamlit.app/',
    'https://zebrafish-3d-morphometry-suite-yash.streamlit.app/',
    'https://huntington-research-app-backup.streamlit.app/',
    'https://huntington-research-app.streamlit.app/'
]

def wake_apps():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        for url in urls:
            try:
                print(f"Checking: {url}")
                # networkidle ensures the Streamlit 'loading' spinner is gone
                page.goto(url, wait_until="networkidle", timeout=90000)
                time.sleep(5)
                print(f"✅ Awake: {url}")
            except Exception as e:
                print(f"❌ Error waking {url}: {e}")
        browser.close()

if __name__ == "__main__":
    wake_apps()
