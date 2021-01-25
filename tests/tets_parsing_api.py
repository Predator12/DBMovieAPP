import requests

if __name__ == "__main__":
    url = "https://imdb8.p.rapidapi.com/title/auto-complete"

    querystring = {"q": "Spiderman 3"}

    headers = {
        'x-rapidapi-key': "f539267541msh52b191adb352b1bp194e4ejsnc6e67f8f462f",
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
    }

    response = requests.request(
        "GET",
        url,
        headers=headers,
        params=querystring
    )

    print(response.json())
    title_filme = ""
    for date in response.json().get("d"):
        if date.get("y") == 2007:
            title_filme = date.get("id")
            break

    url_get_rating = "https://imdb8.p.rapidapi.com/title/get-ratings"
    response = requests.request(
        "GET",
        url_get_rating,
        headers=headers,
        params={"tconst": title_filme}
    )

    print(response.status_code)
    rate = response.json().get("rating")
    print(rate)
