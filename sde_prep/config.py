"""Configuration for SDE Interview Prep Tracker."""
from pathlib import Path
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""

    # Paths
    app_dir: Path = Path(__file__).resolve().parent
    templates_dir: Path = app_dir / "templates"
    static_dir: Path = app_dir / "static"

    # App
    app_name: str = "SDE Interview Prep Tracker"
    debug: bool = False
    site_url: str = "http://localhost:8000"

    # Database
    database_url: str = "sqlite:///./sde_prep.db"

    class Config:
        env_file = ".env"


settings = Settings()
