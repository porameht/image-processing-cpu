import os
from RemoveBackground import RemoveBackground
from app.utils.file_handler import FileHandler
from app.services.cloudinary_client import CloudinaryClient

class BackgroundRemoverService:
    def __init__(self):
        self.remover = RemoveBackground()
        self.file_handler = FileHandler()
        self.cloudinary = CloudinaryClient()
    
    def process_image(self, input_path: str, original_filename: str) -> dict:
        """Process image and return output path and cloudinary url"""
        try:
            # Remove background
            image = self.remover.remove_background(input_path)
            
            # Save locally
            output_path = self.file_handler.get_output_path(original_filename)
            image.save(output_path)
            
            # Upload to Cloudinary with unique ID
            upload_result = self.cloudinary.upload_image(
                output_path,
                original_filename=original_filename
            )
            
            # Cleanup local file
            # self.file_handler.cleanup(output_path)
            
            return upload_result
            
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }