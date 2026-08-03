from fastapi import FastAPI
from app.database.db import get_db_connection
from app.api.v1.auth import router as auth_router
from app.api.v1.project import router as project_router
from app.api.v1.document import router as document_router
from app.api.v1.research import router as research_router
from app.api.v1.consulting import router as consulting_router
from app.api.v1.pdf import router as pdf_router
from app.api.v1.dashboard import router as dashboard_router
from app.api.v1.intelligence import router as intelligence_router

app = FastAPI(title="Cognexa.ai",
              version="1.0.0",
              description="EnterPrise AI consultant & research platform")

app.include_router(auth_router)
app.include_router(project_router)
app.include_router(document_router)
app.include_router(research_router) 
app.include_router(consulting_router)
app.include_router(pdf_router)
app.include_router(dashboard_router)
app.include_router(intelligence_router)

@app.on_event("startup")
def startup():
    connection = get_db_connection()
    if connection:
        connection.close()
        print("Database connection closed")

@app.get("/")
def root():

    return {"sucess":"True",
            "Message":"Welcome to Cognexa"}

