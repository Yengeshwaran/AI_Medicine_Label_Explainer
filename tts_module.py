import pyttsx3
import os

AUDIO_FILE = "explanation_audio.mp3"

def text_to_speech(text, output_file=AUDIO_FILE):
    """
    Converts text to speech and saves it to a file.
    
    Args:
        text (str): The text to convert.
        output_file (str): Path to save the audio file.
        
    Returns:
        str: Path to the saved audio file, or None if error.
    """
    try:
        # Initialize the engine
        engine = pyttsx3.init()
        
        # Set properties for "slow, clear speech"
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate - 50)  # Slow down by ~50 wpm
        
        # Save to file (avoids threading issues in Streamlit/Web)
        engine.save_to_file(text, output_file)
        engine.runAndWait()
        
        return output_file
        
    except Exception as e:
        print(f"Error in TTS: {e}")
        return None
