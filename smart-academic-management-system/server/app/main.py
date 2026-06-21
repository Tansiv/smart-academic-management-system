from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "SAMS Backend Running"}  