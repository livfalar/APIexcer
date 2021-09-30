import requests
# Documentation for requests: https://docs.python-requests.org/en/latest/
# When requests.get returns something, what does it return?
# How do I post (put, pathc, delete) with request
# (Just for say) Google query: python requests documentation
from apis import some_function

# Free APIs to explore

BORED_API_URL = "https://www.boredapi.com/api"


def get_some_data(A):
    response = requests.get(
        f"{BORED_API_URL}/activity" # "https://www.boredapi.com/api/activity"
    )
    # Bored API documentation: https://www.boredapi.com
    # THis is a list of APIs that can play with: https://apipheny.io/free-api/

    requests.post(f"{BASE_API_URL}/post", {"some": "data"})

    # print(response)
    # print(response.status_code)
    data = (response.json)()
    print(data)
    print(data["activity"])
    print(data["type"])
    print(data["participants"])
    print(data["price"])
    print(data["link"])
    print(data["accessibility"])

if __name__ == "__main__":
    # some_function()
    get_some_data('dfkjdf')
    # print("something")
