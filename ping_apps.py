from playwright.sync_api import sync_playwright
import time

urls = [
    'https://scrna-bias-detector.streamlit.app/',
    'https://pangen-ai-yash.streamlit.app/',
    'https://cd40-immunosome-tool-yash.streamlit.app/',
    'https://epicrispr-ml.streamlit.app/',
    'https://zebrafish-3d-morphometry-suite-yash.streamlit.app/',
    'https://huntington-research-app.streamlit.app/',
    'https://tnbc-drug-discovery.streamlit.app/',
    'https://bio-concepts-simplifiedv2-yash.streamlit.app/',
    'https://bio-concepts-simplified-yash.streamlit.app/',
    'https://bio-researcher-database-yash.streamlit.app/',
    'https://bio-tikz-simplifiedv2-yash.streamlit.app/',
    'https://bio-tikz-studio-yash.streamlit.app/',
    'https://huntington-research-app-backup-yash.streamlit.app/',
    'https://immunopet-tracer-optimizer-yash.streamlit.app/',
    'https://multiscale-biodigital-bridge-yash.streamlit.app/',
    'https://neurometabolic-validation-v2-yash.streamlit.app/',
]

def wake_apps():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        for url in urls:
            try:
                print(f"Checking: {url}")
                page.goto(url, wait_until="networkidle", timeout=90000)
                time.sleep(5)
                print(f"✅ Awake: {url}")
            except Exception as e:
                print(f"❌ Error waking {url}: {e}")
        browser.close()

if __name__ == "__main__":
    wake_apps()
