from playwright.sync_api import sync_playwright
import time

# Sirf ye 4 URLs jo sleep par hain
urls = [
    'https://bio-concepts-simplifiedv2-yash.streamlit.app/',
    'https://zebrafish-3d-morphometry-suite-yash.streamlit.app/',
    'https://huntington-research-app-backup.streamlit.app/',
    'https://huntington-research-app.streamlit.app/'
]

def wake_apps():
    with sync_playwright() as p:
        # Browser launch (headless mode)
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
        )
        
        for url in urls:
            page = context.new_page()
            try:
                print(f"🚀 Waking up: {url}")
                # Wait for 60 seconds or until the app fully loads
                page.goto(url, wait_until="networkidle", timeout=90000)
                # Extra 5 seconds to ensure Streamlit 'Spinning' icon disappears
                time.sleep(5) 
                print(f"✅ Success: {url} is now active.")
            except Exception as e:
                print(f"⚠️ Failed to wake {url}: {str(e)}")
            finally:
                page.close()
        
        browser.close()

if __name__ == "__main__":
    wake_apps()
