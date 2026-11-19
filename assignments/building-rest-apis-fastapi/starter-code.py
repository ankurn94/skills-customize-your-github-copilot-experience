from fastapi import FastAPI

app = FastAPI(title="Mergington Library API")


@app.get("/")
def read_root():
    return {"message": "Welcome to the Mergington Library API"}
