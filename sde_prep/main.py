"""SDE Interview Prep Tracker - Main Application"""
from contextlib import asynccontextmanager
from datetime import datetime

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from sde_prep.config import settings
from sde_prep.database import init_db, Base
from sde_prep.routes import sde_prep as sde_prep_routes


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize on startup."""
    init_db()
    yield


app = FastAPI(
    title="SDE Interview Prep Tracker",
    description="Comprehensive interview prep platform",
    version="1.0.0",
    lifespan=lifespan,
)

# Mount static files
app.mount("/static", StaticFiles(directory=str(settings.static_dir)), name="static")

# Templates
templates = Jinja2Templates(directory=str(settings.templates_dir))

# Include routes
app.include_router(sde_prep_routes.router)


@app.get("/")
async def root():
    """Redirect to SDE Prep."""
    return {"message": "SDE Prep Tracker - Visit /tools/sde-prep"}


@app.get("/health")
async def health():
    """Health check."""
    return {"status": "healthy", "service": "SDE Prep Tracker"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
