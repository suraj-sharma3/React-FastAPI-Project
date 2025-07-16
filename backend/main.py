# Tutorial Link : https://github.com/techwithtim/FastAPI-React-Integration/tree/main

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

class Song(BaseModel):
    name: str

class Songs(BaseModel):
    songs: List[Song]
    
app = FastAPI(debug=True)

origins = [
    "http://localhost:5173",
    # Add more origins here
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

memory_db = {"songs": []}

@app.get("/songs", response_model=Songs)
def get_songs():
    return Songs(songs=memory_db["songs"])

@app.post("/songs")
def add_song(song: Song):
    memory_db["songs"].append(song)
    return song
    

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5173)

### Explanation

# This script is a simple FastAPI application for managing a list of songs.

# 1. **Imports**:
#    - `uvicorn`: Runs the FastAPI application with a web server.
#    - `FastAPI`: Creates the application instance.
#    - `CORSMiddleware`: Handles Cross-Origin Resource Sharing (CORS).
#    - `BaseModel` (from Pydantic): Defines and validates data models (schemas).
#    - `List` (from `typing`): Used to define lists of items as type annotations.

# 2. **Data Models**:
#    - `Song` model: Represents a single song with a required string field `name`.
#    - `Songs` model: Represents a collection of songs as a list of `Song` objects.

# 3. **Application Instance**:
#    - A FastAPI app instance is created with debugging enabled.

# 4. **CORS Configuration**:
#    - Specifies allowed origins (e.g., requests from `http://localhost:3000` are allowed).
#    - CORS middleware enables:
#        - Requests from specified origins.
#        - Cookies and authentication headers.
#        - All HTTP methods (e.g., GET, POST).
#        - All headers.

# 5. **In-Memory Database**:
#    - An in-memory dictionary (`memory_db`) is used to store songs as a temporary database.

# 6. **Endpoints**:
#    - `GET /songs`:
#        - Returns the current list of songs in `memory_db`.
#        - Response is serialized into the `Songs` model.
#    - `POST /songs`:
#        - Adds a new song to `memory_db`.
#        - The input is validated against the `Song` model.
#        - Returns the added song.

# 7. **Main Entry Point**:
#    - When the script is run directly, `uvicorn` starts the application.
#    - The app listens on all available network interfaces (`0.0.0.0`) at port 8000.

# 8. **How It Works**:
#    - Start the server by running the script.
#    - Use the `GET /songs` endpoint to retrieve the current list of songs.
#    - Use the `POST /songs` endpoint to add a new song by sending a JSON payload like `{"name": "Song Title"}`.
#    - Check the updated list with another `GET /songs`.

# 9. **Key Features**:
#    - Automatically generated interactive API documentation is available at `/docs` (Swagger UI) and `/redoc` (ReDoc).
#    - Input validation is handled by Pydantic.
#    - CORS middleware ensures secure cross-origin communication.
#    - A simple in-memory database is used for prototyping or small-scale development.
