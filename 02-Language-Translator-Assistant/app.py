import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
client=genai.Client(api_key=GEMINI_API_KEY)

def Language_translator(text,source_language,translated_language):
    prompt=f"Translate the following sentence from {source_language} to {translated_language}\n\n{text}"
    
    response=client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text
    

# topic="Hi How are you"
# user_promt=f"change the sentence {topic} to telugu"
print(Language_translator("Hi, How are You","English","Telugu"))
print(Language_translator("Hi, How are You","English","french"))
print(Language_translator("player scored century","English","Hindi"))