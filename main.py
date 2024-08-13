from fastapi import FastAPI
from Models import models
from Database.mysqlDatabaseConfig import engine
from Routers import a1 # type: ignore

app = FastAPI()
app.include_router(a1.router)
models.Base.metadata.create_all(bind=engine)

@app.get("/")
def api_working_status():
    return {"Status": "Up and Running"}