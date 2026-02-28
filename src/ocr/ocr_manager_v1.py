from base64 import b64encode
from io import BytesIO

from langchain.chat_models import BaseChatModel
from langchain_core.messages import HumanMessage, SystemMessage

from PIL.Image import open as open_image
from PIL.Image import Image

from os import listdir

from re import split

from tqdm import tqdm

from src.chat import get_chat_by_env
from src.interfaces import OCRInterface
from src.ocr.models import Answer, Correction, OCRInput, OCRResult

SYSTEM_PROMPT = """ Você é um motor de OCR especializado em transcrever avaliações.
Sua tarefa é transcrever o texto garantindo a detecção de tokens de controle.

REGRAS:
- Nunca remova caracteres especiais ou pontuação.
- Se vir um símbolo que parece um separador mas está borrado, siga o padrão de formato acima.
- Saída puramente textual, sem introduções.
"""

HUMAN_PROMPT = (
    "Transcreva este documento de avaliação exatamente como está escrito. "
)

def encode_image(image: Image) -> str:
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    return b64encode(buffered.getvalue()).decode('utf-8')

def process_document(image_path: str, chat: BaseChatModel, system_prompt: str) -> str:
    image = open_image(image_path)
    encoded_image = encode_image(image)
    system_message = SystemMessage(content=SYSTEM_PROMPT)
    system_message_2 = SystemMessage(content=system_prompt)
    message = HumanMessage(
        content=[
            {"type": "text", "text": HUMAN_PROMPT},
            {
                "type": "image_url",
                "image_url": f"data:image/jpeg;base64,{encoded_image}"
            },
        ]
    )
    response = chat.invoke([
        system_message,
        system_message_2,
        message])
    return response.content

class OCRManagerV1(OCRInterface):
    def __init__(self):
        super().__init__()

    def ocr(self, ocr_input: OCRInput) -> OCRResult:
        
        system_prompt = f"Nunca ignore os termos que correspondem o seguinte regex: {ocr_input['regex_question']}"
        
        chat = get_chat_by_env()
        
        result: OCRResult = dict()
        
        result["corrections"] = list()
        
        students_path = ocr_input["ocr_path"]
        
        students = [student for student in listdir(students_path)]
        
        for student in tqdm(students, desc="Processing students", total=len(students)):
            student_path = f"{ocr_input['ocr_path']}/{student}"
            
            correction_turn: Correction = dict()
            result["corrections"].append(correction_turn)
            
            correction_turn["student_id"] = student
            correction_turn["answers"] = list()
            
            last_answer: Answer = None
            
            for page in sorted(listdir(student_path)):
                page_path = f"{student_path}/{page}"
                
                page_text = process_document(page_path, chat, system_prompt)
                
                answers = split(ocr_input["regex_question"], page_text)
                
                for answer in answers[1:]:
                    answer_correction: Answer = {"answer": answer, "question_id": len(correction_turn["answers"])}
                    correction_turn["answers"].append(answer_correction)
                
                if last_answer:
                    last_answer["answer"] += answers[0]
                
                if any(correction_turn["answers"]):
                    last_answer = correction_turn["answers"][-1]
                
        return result