import json
import os
import requests
import datetime
from utility import get_session
from models import Actor, Movie, Director


def date_setup(splite_date, cur_daete):
    if len(splite_date) == 2:
        splite_date[1] = splite_date[1].replace("3", "-")
        cur_daete = "-".join(splite_date)

    splite_date = cur_daete.split("-")
    if int(splite_date[1]) <= 12:
        current_date = datetime.datetime.strptime(cur_daete, '%Y-%m-%d')
    else:
        current_date = datetime.datetime.strptime(cur_daete, '%Y-%d-%m')
        
    return current_date


if __name__ == "__main__":
    session = get_session()
    result = {}
    with open("movies.json") as json_file:
        result = json.load(json_file)

    print(result)
    for movie in result["result"]:
        try:
            split_date = movie.get("release-date").split("-")
            cur_daete = movie.get("release-date")
            current_date = date_setup(split_date, cur_daete)
        except:
            current_date = datetime.datetime(2017,3,2)

        movie_model = Movie(
            movie.get("name"),
            movie.get("storyline")if movie.get("storyline") else "unknown",
            current_date.date()
        )

        session.add(movie_model)
        for actor in movie["actors"]:

            if type(actor) is str:
                actor_name = actor.split(" ")
                try:
                    actor_model = session.query(Actor).filter(first_name=actor_name[0], last_name=actor_name[1]).scalar()
                except:
                    actor_model = Actor(actor_name[0], actor_name[-1], datetime.datetime(1987, 3, 2), "unknown")
                    session.add(actor_model)
            else:
                actor_name = actor.get("name").split(" ")
                try:
                    actor_model = session.query(
                        Actor
                    ).filter(
                        first_name=actor_name[0],
                        last_name=actor_name[1]
                    ).scalar()
                except:
                    try:
                        split_date = movie.get("birthdate").split("-")
                        cur_daete = movie.get("birthdate")

                        current_date = date_setup(split_date, cur_daete)
                    except:
                        current_date = datetime.datetime(1987, 3, 2)

                    actor_model = Actor(
                        actor_name[0],
                        actor_name[-1],
                        current_date.date(),
                        actor.get(
                            "birthplace"
                        ).split(",")[-1].replace(" ", ""))
                    session.add(actor_model)

            movie_model.actors.append(actor_model)

        if movie.get("directors"):
            for director in movie["directors"]:
                if type(director) is str:
                    director_name = director.split(" ")
                    try:
                        director_model = session.query(
                            Director
                        ).filter(
                            first_name=director_name[0],
                            last_name=director_name[1]
                        ).scalar()
                    except:
                        director_model = Director(
                            director_name[0],
                            director_name[-1],
                            datetime.datetime(1987, 3, 2),
                            "unknown")
                        session.add(director_model)
                else:
                    director_name = director.get("name").split(" ")
                    try:
                        director_model = session.query(
                            Director
                        ).filter(
                            first_name=director_name[0],
                            last_name=director_name[1]
                        ).scalar()
                    except:
                        try:
                            split_date = movie.get("birthdate").split("-")
                            cur_daete = movie.get("birthdate")
                            current_date = date_setup(split_date, cur_daete)
                        except:
                            current_date = datetime.datetime(1987, 3, 2)

                        director_model = Director(
                            director_name[0],
                            director_name[-1],
                            current_date.date(),
                            director.get(
                                "birthplace"
                            ).split(",")[-1].replace(" ", "")
                        )
                        session.add(director_model)
                movie_model.directors.append(director_model)

        elif movie.get("director"):
            if type(movie["director"]) is str:
                director_name = movie["director"].split(" ")
                try:
                    director_model = session.query(
                        Director
                    ).filter(
                        first_name=director_name[0],
                        last_name=director_name[1]
                    ).scalar()

                    session.add(director_model)
                except:
                    director_model = Director(
                        director_name[0],
                        director_name[-1],
                        datetime.datetime(1987, 3, 2),
                        "unknown"
                    )
                    # session.add(director_model)

                movie_model.directors.append(director_model)
            else:
                for director in movie["director"]:
                    if type(director) is str:
                        director_name = director.split(" ")
                        try:
                            director_model = session.query(
                                Director
                            ).filter(
                                first_name=director_name[0],
                                last_name=director_name[1]
                            ).scalar()
                        except:
                            director_model = Director(
                                director_name[0],
                                director_name[-1],
                                datetime.datetime(1987, 3, 2),
                                "unknown"
                            )
                            session.add(director_model)
                    else:
                        director_name = director.get("name").split(" ")
                        try:
                            director_model = session.query(
                                Director
                            ).filter(
                                first_name=director_name[0],
                                last_name=director_name[1]
                            ).scalar()
                        except:
                            try:
                                split_date = director.get(
                                    "birthdate"
                                ).split("-")
                                cur_daete = director.get("birthdate")
                                current_date = date_setup(
                                    split_date,
                                    cur_daete
                                )
                            except BaseException as e:
                                current_date = datetime.datetime(1987, 3, 2)

                            director_model = Director(
                                director_name[0],
                                director_name[-1],
                                current_date.date(),
                                director.get(
                                    "birthplace"
                                ).split(",")[-1].replace(" ", "")
                            )
                            session.add(director_model)

                    movie_model.directors.append(director_model)

        session.commit()
