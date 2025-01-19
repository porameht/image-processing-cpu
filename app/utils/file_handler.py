import os
from fastapi import UploadFile
from app.core.config import settings

class FileHandler:
    def __init__(self):
        self.temp_dir = settings.TEMP_DIR
        self.output_dir = settings.OUTPUT_DIR
        self._ensure_directories()
    
    def _ensure_directories(self):
        """Ensure necessary directories exist"""
        for directory in [self.temp_dir, self.output_dir]:
            if not os.path.exists(directory):
                os.makedirs(directory)
    
    async def save_upload(self, file: UploadFile) -> str:
        """Save uploaded file and return the path"""
        temp_path = os.path.join(self.temp_dir, file.filename)
        with open(temp_path, "wb") as buffer:
            content = await file.read()
            buffer.write(content)
        return temp_path
    
    def get_output_path(self, filename: str) -> str:
        """Generate output file path"""
        filename_no_ext = os.path.splitext(filename)[0]
        return os.path.join(self.output_dir, f"{filename_no_ext}_nobg.png")
    
    def cleanup(self, filepath: str):
        """Remove temporary files"""
        if os.path.exists(filepath):
            os.remove(filepath) 