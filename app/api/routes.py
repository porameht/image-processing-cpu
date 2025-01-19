from fastapi import APIRouter, UploadFile, File
from app.services.background_remover import BackgroundRemoverService
from app.utils.file_handler import FileHandler

router = APIRouter()

@router.get("/")
def read_root():
    return {"status": "ok"}

@router.post("/remove-bg")
async def remove_bg(file: UploadFile = File(...)):
    try:
        file_handler = FileHandler()
        bg_remover = BackgroundRemoverService()
        
        # Save uploaded file
        temp_path = await file_handler.save_upload(file)
        
        # Process image and upload to Cloudinary
        result = bg_remover.process_image(temp_path, file.filename)
        
        # Cleanup temporary file
        file_handler.cleanup(temp_path)
        
        return result
        
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        } 