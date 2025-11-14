from pytesseract import image_to_string

from PIL.Image import open

from src.interfaces import OCRInterface

from src.settings import Settings

class OCRManagerV0(OCRInterface):
    def ocr(self, image_file_path: str):
        image_bytes = open(image_file_path)
        return image_to_string(image_bytes, lang=Settings.tesseract_language, config=Settings.tesseract_configuration)