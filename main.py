from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Podés restringir después
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = "AIzaSyAM573d-J5YCPbJfDh3AiAWcfs8DcxE3Wo"  # Tu key de Google Places

@app.get("/api/places")
def get_places(q: str):
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={q}&type=store&key={API_KEY}"
    r = requests.get(url)
    return r.json()
