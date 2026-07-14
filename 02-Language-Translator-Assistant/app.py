
import os
from google import genai
from dotenv import load_dotenv
from google.genai import types
import gradio as gr 


load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)

languages={
    "Hindi":"Translate the following sentence into Hindi",
    "Telugu":"Translate the following sentence into Telugu",
    "French":"Translate the following sentence into French"
    }

def translate_text(question,language):
    system_prompt=languages[language]
    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            config=types.GenerateContentConfig(
                system_instruction=system_prompt
            ),
            contents=question
        )
        return response.text

    except Exception:
        return (
            "Gemini is currently unavailable or busy. "
            "Please try again after a few moments."
        )

demo=gr.Interface(
    fn=translate_text,
    inputs=[gr.Textbox(lines=4,placeholder="Enter text to translate",label="Input Text"),
            gr.Dropdown(list(languages.keys()),label="Target Language",value="Telugu")
            ],
    outputs=gr.Textbox(lines=6,label="Translated Text"),
    title="Language Translator Assistant",
    description="Translate text into different languages using Google's Gemini AI."

)

demo.launch(debug=True)