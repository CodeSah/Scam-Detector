import requests

API_KEY = "your_google_safe_browsing_api_key"

def check_url(url):
    payload = {
        "client": {"clientId": "your_project", "clientVersion": "1.0"},
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}]
        }
    }
    resp = requests.post(
        f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={API_KEY}",
        json=payload
    )
    return {"safe": not resp.json()}