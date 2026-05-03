# Function to translate text from English to Tamil
from googletrans import Translator
def translate_to_tamil(text):
    translator = Translator()
    try:
        # Translate the text from English to Tamil
        translated = translator.translate(text, src='en', dest='ta')  # 'ta' is the language code for Tamil
        translated_text = translated.text
        
        # Print the translation
        print(f"Original Text: {text}")
        print(f"Translated Text (Tamil): {translated_text}")
        
        # Return the translated text
        return translated_text
    
    except Exception as e:
        # If there's an error, print the error message
        print("Error in translation:", e)
        return None