import requests

def main():
    url = "https://example.org"
    r = requests.get(url)
    print("Status code:", r.status_code)
    print("First 100 chars of page:", r.text[:100])

if __name__ == "__main__":
    main()
