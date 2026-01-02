import pytesseract
from PIL import Image
import io

# NOTE: If Tesseract is not in your PATH, you might need to specify the path manually.
# Example: pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text(image_input):
    """
    Extracts text from an image using Tesseract OCR.
    
    Args:
        image_input: Can be a file path (str), bytes, or a PIL Image object.
        
    Returns:
        str: The extracted and cleaned text.
    """
    try:
        # Load the image
        if isinstance(image_input, (str, bytes, io.BytesIO)):
            image = Image.open(image_input)
        else:
            image = image_input

        # Perform OCR
        # lang='eng' by default, but Tesseract supports others. 
        # For medicine labels, English is the primary target.
        text = pytesseract.image_to_string(image)
        
        # Clean basic noise
        cleaned_text = _clean_text(text)
        
        return cleaned_text
        
    except Exception as e:
        return f"Error during OCR processing: {str(e)}"

def _clean_text(text):
    """
    Basic cleaning of extracted text.
    """
    if not text:
        return ""
        
    # Remove leading/trailing whitespace
    lines = text.split('\n')
    
    # Filter out empty lines or very short lines (often noise)
    cleaned_lines = [line.strip() for line in lines if len(line.strip()) > 2]
    
    return "\n".join(cleaned_lines)

if __name__ == "__main__":
    # Simple test block
    print("OCR Module Loaded. Run via app.py")
