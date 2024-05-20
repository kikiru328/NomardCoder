import requests

URL = "https://nomad-movies.nomadcoders.workers.dev/movies"

movie_ids = [238, 680, 550, 185, 641, 515042, 152532, 120467, 872585, 906126, 840430]

properties = ("title", "overview", "vote_average")

for movie_id in movie_ids:
    property_dict = {}
    api = f"{URL}/{movie_id}"
    response = requests.get(api)
    if response.status_code != 200:
        print(movie_id)
    else:
        print(f"Movie ID : {movie_id}")
        movie_info = response.json()
        for property in properties:
            if property in movie_info:
                print(f"{property} : {movie_info[property]}")
            else:
                print(f"{property} : N/A")
    print()
