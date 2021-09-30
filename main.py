from requests import get

def get_some_data():
    res = get("https://api.publicapis.org/entries")
    print(res.status)
    print(res.data)

if __name__ == "__main__":
    print("something")