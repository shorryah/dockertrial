from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI() 

origins = [
    "http://localhost",          
    "http://localhost:3000",     
    "http://localhost:8080", 
    "http://192.168.30.1:5173",
    "http://192.168.137.1:5173",
    "http://192.168.29.139:5173",
    "http://172.27.160.1:5173"    
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"],   
    allow_headers=["*"],  
)
movies = [{"title": "Inception", "direction": "Christopher Nolan", "year": 2010},
    {"title": "The Matrix", "direction": "The Wachowskis", "year": 1999}]

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
