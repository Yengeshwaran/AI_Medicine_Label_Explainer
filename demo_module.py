from PIL import Image
import os

ASSETS_DIR = os.path.join(os.path.dirname(__file__), 'assets')
SAMPLE_IMAGE_PATH = os.path.join(ASSETS_DIR, 'sample_label.png')

def get_demo_image():
    """
    Loads and returns the sample medicine label image.
    """
    try:
        if os.path.exists(SAMPLE_IMAGE_PATH):
            return Image.open(SAMPLE_IMAGE_PATH)
        else:
            return None
    except Exception as e:
        print(f"Error loading demo image: {e}")
        return None
