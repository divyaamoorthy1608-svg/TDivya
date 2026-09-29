from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

from app.routes.planner_route import router as planner_router

app = FastAPI(title="PocketSmart AI")

# Include all planner routes
app.include_router(planner_router)

# Mount static if exists
if os.path.exists("app/static"):
    app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

@app.get("/")
async def root():
    return {"message": "💰 PocketSmart AI - Your Smart Budget & Recommendation Assistant - Project is running successfully!"}

@app.get("/health")
async def health():
    return {"status": "ok"}