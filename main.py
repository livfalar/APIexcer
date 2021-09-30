from requests import get

# Free APIs to explore

BORED_API_URL = "https://www.boredapi.com/api"


def get_some_data():
    res = get(f"{BORED_API_URL}/activity")
    print(res)
    print(res.status_code)
    print(res.json())

if __name__ == "__main__":
    get_some_data()
    print("something")