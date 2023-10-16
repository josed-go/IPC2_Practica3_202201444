from clases.movie import movie

import json

class movie_controller:
    def __init__(self):
        self.movies = []

    def add_movie(self, id_movie, name, genre):
        for movie_ in self.movies:
            if movie_.name.lower() == name.lower() or movie_.id_movie == id_movie:
                return False
            

        newMovie = movie(id_movie, name, genre)

        self.movies.append(newMovie)
        return True
    
    # def update_movie(self, id_movie, name, genre):
    #     for movie in self.movies:
    #         if movie.name == name or movie.id_movie == id_movie:
    #             return False
    
    def movies_by_genre(self, genre):
        return json.dumps([movie.dump() for movie in self.movies if movie.genre.lower() == genre.lower()], indent = 4)