import requests


API_KEY = "f539267541msh52b191adb352b1bp194e4ejsnc6e67f8f462f"
API_HOST = "imdb8.p.rapidapi.com"


def get_movie_rating(movie_name, creation_date):
    movie_rate = "-"
    movie_year = str(creation_date.year)

    try:
        url_search_film = "https://imdb8.p.rapidapi.com/title/auto-complete"
        querystring = {"q": movie_name}
        headers = {
            'x-rapidapi-key': API_KEY,
            'x-rapidapi-host': API_HOST
        }
        response = requests.request(
            "GET",
            url_search_film,
            headers=headers,
            params=querystring)
        title_movie_id = ""
        for data in response.json().get("d"):

            if str(data.get("y", "")) == movie_year:
                title_movie_id = data.get("id")
                break

        if title_movie_id:
            url_get_rating = "https://imdb8.p.rapidapi.com/title/get-ratings"
            response = requests.request(
                "GET",
                url_get_rating,
                headers=headers,
                params={"tconst": title_movie_id}
            )
            movie_rate = str(response.json().get("rating"))

    except BaseException as e:
        movie_rate = str(e)

    return movie_rate
