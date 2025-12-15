import requests
import pandas as pd

def scrape_remoteok_api():
    url = "https://remoteok.com/api"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    print("Status Code:", response.status_code)

    data = response.json()

    jobs = []

    for item in data:
        # آیتم اول متادیتاست، شغل نیست
        if "id" not in item:
            continue

        jobs.append({
            "id": item.get("id"),
            "title": item.get("position"),
            "company": item.get("company"),
            "location": item.get("location"),
            "tags": ", ".join(item.get("tags", [])),
            "url": item.get("url")
        })

    df = pd.DataFrame(jobs)
    df.to_csv("remoteok_jobs.csv", index=False, encoding="utf-8-sig")

    print(f"{len(df)} jobs scraped successfully!")

if __name__ == "__main__":
    scrape_remoteok_api()
