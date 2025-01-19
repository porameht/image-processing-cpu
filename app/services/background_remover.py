from RemoveBackground import RemoveBackground
from app.utils.file_handler import FileHandler

class BackgroundRemoverService:
    def __init__(self):
        self.remover = RemoveBackground()
        self.file_handler = FileHandler()
    
    def process_image(self, input_path: str, original_filename: str) -> str:
        """Process image and return output path"""
        image = self.remover.remove_background(input_path)
        
        output_path = self.file_handler.get_output_path(original_filename)
        image.save(output_path)
        
        return output_path