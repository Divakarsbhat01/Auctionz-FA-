from fastapi import FastAPI # type: ignore

app = FastAPI()

@app.get("/")
def abcd():
    return {"Status":"Up"}