from fastapi import APIRouter, FastAPI,upload_file
import os
import helpers.config import get_settings,settings




data_router = APIRouter(
    prefix="/api/v1",
    tags=["Base","data"],
)


@data_router.get("/")
async  def welcome_message():
    app_name=os.getenv("APP_NAME", "FastAPI Application")
    app_version=os.getenv("APP_VERSION", "1.0.0") 
    return {"message": f"Welcome to the {app_name} v{app_version}!"}

#hi
