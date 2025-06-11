from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

app = FastAPI()  

movies = []

class Movie(BaseModel):
    title: str
    direction: str 
    year: int

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/movies", response_model=List[Movie])
def get_movies():
    return movies

@app.post("/addmovie")
def add_movie(movie: Movie):
    for m in movies:
        if m.title == movie.title and m.direction == movie.direction and m.year == movie.year:
            return {"message": "Movie already exists!"}
    movies.append(movie)
    return {"message": "Movie added successfully"}
