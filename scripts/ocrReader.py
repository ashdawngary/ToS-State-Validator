'''
actual adapter for tesseract.  Utilizes pytesseract and will assert if this isnt configured correctly.
'''
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
def readImage(im):
    return pytesseract.image_to_string(im)
