import requests
import time

# List all your Streamlit App URLs here
apps = [
    "https://bio-concepts-simplifiedv2-yash.streamlit.app/",
    "https://bio-researcher-database-yash.streamlit.app/",
    "https://bio-tikz-simplifiedv2-yash.streamlit.app/",
    "https://bio-tikz-studio-yash.streamlit.app/",
    "https://cd40-immunosome-tool.streamlit.app/",
    "https://huntington-research-app.streamlit.app/"
]

def wake_apps():
    for url in apps:
        try:
            response = requests.get(url, timeout=20)
            if response.status_code == 200:
                print(f"Successfully pinged: {url}")
            else:
                print(f"Failed to ping {url}: Status {response.status_code}")
        except Exception as e:
            print(f"Error pinging {url}: {e}")

if __name__ == "__main__":
    wake_apps()
