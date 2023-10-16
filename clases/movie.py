class movie: 
    def __init__(self, id_movie, name, genre):
        self.id_movie = id_movie
        self.name = name
        self.genre = genre

    def dump(self):
        return {
            "movieId": self.id_movie,
            "name": self.name,
            "genre": self.genre
        }