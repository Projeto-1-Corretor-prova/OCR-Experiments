from abc import ABC

from src.preprocess.models import PreProcesserInput

from src.ocr.models import OCRInput, OCRResult

class PreProcessInterface(ABC):
    def preprocess(self, pre_processer_input: PreProcesserInput) -> None:
        """Pre Process pictures for future OCR

        Args:
            pre_processer_input (PreProcesserInput): Pre process input

        """
        raise NotImplementedError("This is just a interface method!")
    
class OCRInterface(ABC):
    def ocr(self, ocr_input: OCRInput) -> OCRResult:
        """ Generate the OCR from pictures

        Args:
            ocr_input (OCRInput): OCR input
            
        Returns:
            OCRResult: OCR result
        """
        raise NotImplementedError("This is just a interface method!")