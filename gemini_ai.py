import google.generativeai as genai
import os
from PIL import Image
from gtts import gTTS 

def configure_gemini(api_key):
    if not api_key:
        return False
    os.environ["GOOGLE_API_KEY"] = api_key
    genai.configure(api_key=api_key)
    return True

def analyze_hand_image(image_data):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash') 
        prompt = "Analyze this image..." # (Shortened for brevity)
        img = Image.open(image_data)
        response = model.generate_content([prompt, img])
        return response.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

def fix_grammar(text_input):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(f"Convert this sign gloss to English: {text_input}")
        return response.text.strip()
    except Exception as e:
        return str(e)

def text_to_speech(text):
    """
    Converts text to an audio byte stream using Google TTS.
    """
    try:
        tts = gTTS(text=text, lang='en')
        audio_fp = io.BytesIO()
        tts.write_to_fp(audio_fp)
        audio_fp.seek(0)
        return audio_fp
    except Exception as e:
        return None