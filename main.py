from fastapi import FASTAPI
from typing import List
from pydantic import BaseModel


movies = []

class Movie(BaseModel):
    title: str
    direction: str 
    year: int
app = FastAPI()


@app.get("/movies", repsonse_model=List[Movie])
def get_movies():
    return movies

@app.post("/addmovie")
def add_movie(movie:Movie):
    movies.append(movies)
    return {"message": "Movie added successfully"}
