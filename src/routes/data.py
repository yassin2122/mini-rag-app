from fastapi import APIRouter, Depends, FastAPI, UploadFile,upload_file
import os
import helpers.config import get_settings,settings
from controllers import DataController




data_router = APIRouter(
    prefix="/api/v1",
    tags=["Base","data"],
)
@data_router.post("/upload/{file_name}")
async def upload_file(file_name: str, file: UploadFile,
                      app_settings: settings = Depends(get_settings)):


    is_valid =DataController().validate_file(file=file)

    
    # Implement your file upload logic here
    return {"message": f"File '{file_name}' uploaded successfully."}


    #hii