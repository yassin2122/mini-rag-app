
from .BaseController import Basecontroller
from fastapi import UploadFile, HTTPException




class DataController(Basecontroller):
    def __init__(self):
        super().__init__()

    def validate_file(self, file: UploadFile):
        # Validate file extension
        if file.content_type not in self.settings.FILE_ALLOWED_TYPES:
            raise HTTPException(status_code=400, detail="Invalid file type.")
        
        # Validate file size
        if len(file.file.read()) > self.settings.FILE_MAX_SIZE * 1024 * 1024:
            raise HTTPException(status_code=400, detail="File size exceeds the maximum limit.")
        
        # Reset the file pointer to the beginning after reading
        file.file.seek(0)