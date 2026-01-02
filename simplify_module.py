import requests
import json

def simplify_text(text, language="English", model="mistral"):
    """
    Simplifies medical text using a local LLM via Ollama.
    
    Args:
        text (str): The OCR extracted text.
        language (str): Target language ('English' or 'Tamil').
        model (str): Name of the Ollama model to use (default: 'mistral').
        
    Returns:
        str: Simplified explanation or error message.
    """
    if not text:
        return "No text provided to simplify."

    api_url = "http://localhost:11434/api/generate"
    
    # SYSTEM PROMPT: Defines the persona and safety rules
    system_instruction = (
        "You are a helpful assistant for elderly patients. "
        "Your task is to rewrite the given medicine label text in extremely simple, easy-to-understand language. "
        "Rules:\n"
        "1. DO NOT change any dosage information (numbers, mg, times per day).\n"
        "2. DO NOT give medical advice beyond what is on the label.\n"
        "3. DO NOT diagnose diseases or recommend medicines.\n"
        "4. Only explain what is written on the medicine label.\n"
        "5. Emphasize warnings (like 'Keep out of reach of children').\n"
        "6. If the text is messy code or noise, say 'Could not read the label clearly'.\n"
        "7. Format the output using these clear headers:\n"
        "   ## 💊 Medicine Name\n"
        "   ## 🩺 What it is for\n"
        "   ## 🕒 How to take\n"
        "   ## ⚠️ Important note\n"
    )

    if language.lower() == "tamil":
        user_prompt = (
            f"{system_instruction}\n"
            "Translate the simplified explanation into clear, spoken-style Tamil (Tamil script).\n\n"
            f"Here is the text to explain:\n{text}"
        )
    else:
        user_prompt = (
            f"{system_instruction}\n"
            "Keep the output in simple English.\n\n"
            f"Here is the text to explain:\n{text}"
        )

    # JSON payload for Ollama
    payload = {
        "model": model,
        "prompt": user_prompt,
        "stream": False
    }

    try:
        response = requests.post(api_url, json=payload)
        response.raise_for_status()
        
        result = response.json()
        return result.get("response", "Error: Empty response from AI.")
        
    except requests.exceptions.ConnectionError:
        return (
            "Error: Could not connect to local AI service. "
            "Please make sure Ollama is running (run 'ollama serve' in terminal)."
        )
    except Exception as e:
        return f"Error during simplification: {str(e)}"

if __name__ == "__main__":
    # Test block
    sample_text = "Rx: Amoxicillin 500mg. Take 1 tablet every 8 hours for 7 days. Warning: May cause drowsiness."
    print("Testing English Simplification...")
    print(simplify_text(sample_text, "English"))
    # print("\nTesting Tamil Simplification...")
    # print(simplify_text(sample_text, "Tamil"))
