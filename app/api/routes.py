from fastapi import APIRouter, UploadFile, File
from app.services.background_remover import BackgroundRemoverService
from app.utils.file_handler import FileHandler
from app.core.config import settings

router = APIRouter()

@router.get("/")
def read_root():
    return {"status": "ok"}

@router.post("/remove-bg")
async def remove_bg(file: UploadFile = File(...)):
    try:
        file_handler = FileHandler()
        bg_remover = BackgroundRemoverService()
        
        temp_path = await file_handler.save_upload(file)
        
        output_path = bg_remover.process_image(temp_path, file.filename)
        
        file_handler.cleanup(temp_path)
        
        return {
            "status": "success",
            "file": output_path
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        } 