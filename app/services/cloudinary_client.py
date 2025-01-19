import cloudinary
import cloudinary.uploader
from app.core.config import settings
from app.utils.id_generator import generate_unique_id

class CloudinaryClient:
    def __init__(self):
        cloudinary.config(
            cloud_name=settings.CLOUDINARY_CLOUD_NAME,
            api_key=settings.CLOUDINARY_API_KEY,
            api_secret=settings.CLOUDINARY_API_SECRET,
            secure=True
        )
    
    def upload_image(self, image_path: str, original_filename: str = None) -> dict:
        """
        Upload an image to Cloudinary and return the response
        """
        try:
            # Generate unique ID using original filename as prefix
            prefix = original_filename.split('.')[0] if original_filename else "img"
            unique_id = generate_unique_id(prefix)
            
            upload_result = cloudinary.uploader.upload(
                image_path,
                public_id=unique_id,
                folder="background-remover",
                resource_type="image"
            )
            return {
                "status": "success",
                "url": upload_result["secure_url"],
                "public_id": upload_result["public_id"],
                "original_filename": original_filename
            }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            } 