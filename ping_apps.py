import asyncio
from playwright.async_api import async_playwright

urls = [
    'https://scrna-bias-detector.streamlit.app/',
    'https://pangen-ai-yash.streamlit.app/',
    'https://cd40-immunosome-tool-yash.streamlit.app/',
    'https://epicrispr-ml.streamlit.app/',
    'https://oral-nanopharm-pipeline.streamlit.app/',
    'https://zebrafish-3d-morphometry-suite-yash.streamlit.app/',
    'https://huntington-research-yash.streamlit.app/',
    'https://tnbc-drug-discovery.streamlit.app/',
    'https://bio-concepts-simplified-v2-yash.streamlit.app/',
    'https://bio-concepts-simplified-yash.streamlit.app/',
    'https://bio-researcher-database-yash.streamlit.app/',
    'https://bio-tikz-simplifiedv2-yash.streamlit.app/',
    'https://bio-tikz-studio-yash.streamlit.app/',
    'https://huntington-research-app-backup-yash.streamlit.app/',
    'https://immunopet-tracer-optimizer-yash.streamlit.app/',
    'https://multiscale-biodigital-bridge-yash.streamlit.app/',
    'https://neurometabolic-validation-v2-yash.streamlit.app/',
]

# Cap how many pages open at once so the runner doesn't get overloaded
CONCURRENCY = 5


async def ping_one(browser, url, semaphore):
    async with semaphore:
        page = await browser.new_page()
        try:
            # domcontentloaded instead of networkidle -- Streamlit keeps a
            # websocket connection open, so networkidle basically never
            # fires cleanly and just burns time waiting for the timeout.
            await page.goto(url, wait_until="domcontentloaded", timeout=45000)
            # Small wait to let the Streamlit app actually wake up / render
            await page.wait_for_timeout(4000)
            print(f"✅ Awake: {url}")
        except Exception as e:
            print(f"❌ Error waking {url}: {e}")
        finally:
            await page.close()


async def wake_apps():
    semaphore = asyncio.Semaphore(CONCURRENCY)
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        tasks = [ping_one(browser, url, semaphore) for url in urls]
        await asyncio.gather(*tasks)
        await browser.close()


if __name__ == "__main__":
    asyncio.run(wake_apps())
