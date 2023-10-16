from clases.movie import movie

import json

class movie_controller:
    def __init__(self):
        self.movies = []

    def get_movie(self, id_movie):
        for movie in self.movies:
            if str(movie.id_movie) == str(id_movie):
                return {
                    "movieId": movie.id_movie,
                    "name": movie.name,
                    "genre": movie.genre
                }
            
    def get_movies(self):
        return json.dumps([movie.dump() for movie in self.movies], indent = 4)

    def add_movie(self, id_movie, name, genre):
        for movie_ in self.movies:
            if movie_.name.lower() == name.lower() or movie_.id_movie == id_movie:
                return False
            

        newMovie = movie(id_movie, name, genre)

        self.movies.append(newMovie)
        return True
    
    def movies_by_genre(self, genre):
        return json.dumps([movie.dump() for movie in self.movies if movie.genre.lower() == genre.lower()], indent = 4)
    
    def update_movie(self, id_movie, new_name, new_genre):
        for movie in self.movies:
            if str(movie.id_movie) == str(id_movie):
                movie.name = new_name
                movie.genre = new_genre
                return True
            
        return False