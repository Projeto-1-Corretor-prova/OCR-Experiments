from abc import ABC

from src.ocr.models import OCRInput, OCRResult
    
class OCRInterface(ABC):
    def ocr(self, ocr_input: OCRInput) -> OCRResult:
        """ Generate the OCR from pictures

        Args:
            ocr_input (OCRInput): OCR input
            
        Returns:
            OCRResult: OCR result
        """
        raise NotImplementedError("This is just a interface method!")