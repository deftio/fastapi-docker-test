from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os
import random

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def read_index():
    # Serve the index.html file directly from the root path
    return FileResponse(os.path.join('static', 'index.html'))



@app.get("/random")
async def read_random(max: int = Query(default=100, ge=0)):
    """
    Returns a random number between 0 and 'max'.
    The 'max' parameter must be greater than or equal to 0.
    """
    return {"random_number": random.randint(0, max)}

@app.get("/named_random")
async def read_named_random(name: str = Query(default="no_name", min_length=0)):
    """
    Returns a JSON object with a 'name' value and a 'value' key 
    representing a random number between 0 and 1000.
    """
    random_number = random.randint(0, 1000)
    return {"name": name, "value": random_number}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)