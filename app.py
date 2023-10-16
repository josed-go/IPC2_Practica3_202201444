from flask import Flask
from flask_cors import CORS
from controladores.movie_controller import movie_controller
from flask.globals import request

movie_handler = movie_controller()

app = Flask(__name__)
CORS(app)

movie_handler.add_movie(1, 'Rey leon', 'Animado')
movie_handler.add_movie(2, 'Saw', 'Terror')
movie_handler.add_movie(3, 'Ready Player One', 'Ficcion')
movie_handler.add_movie(4, 'Pinocho', 'Animado')

@app.route("/")
def index():
    return "<h1>Backend</h1>"

@app.route("/new-movie", methods = ['POST'])
def new_movie():
    response = {}
    id_movie = request.json['movieId']
    name = request.json['name']
    genre = request.json['genre']
    if (movie_handler.add_movie(id_movie, name, genre)):
        response={
            "state": 200,
            "message": "Pelicula agregada con exito",
            "movie": movie_handler.get_movie(id_movie)
        }
    else:
        response={
            "state": "Error",
            "message": "La pelicula ya existe o ID invalido"
        }
    return response

@app.route("/all-movies-by-genre/<genre>", methods = ['GET'])
def movies_by_genre(genre):
    movies = movie_handler.movies_by_genre(genre)
    response = {}
    if(len(movies) > 2):
        return movies
    else:
        response={
            "state": "!!!",
            "message": "No existen peliculas con ese genero"
        }
    return response

if __name__ == '__main__':
    app.run(threaded = True, port = 5000, debug = True)