import requests

try:
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)

    if response.status_code == 200:
        users = response.json()

        for user in users:
            if user["address"]["city"] == "Gwenborough":
                print(user["name"])
                print(user["email"])
                print(user["phone"])
                print(user["Company"], ["name"])

            else:
                print("failed to fetch data")
except Exception as e:
    print("Error", e)

