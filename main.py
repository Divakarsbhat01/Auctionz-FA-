from fastapi import FastAPI

from Routers import a1 # type: ignore

app = FastAPI()
app.include_router(a1.router)

@app.get("/")
def api_working_status():
    return {"Status": "Up and Running"}