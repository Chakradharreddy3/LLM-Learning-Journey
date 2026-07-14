import os 
from google import genai
from google.genai import types 
import gradio as gr
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")


question_type={
    "MCQs":
        """
        You are an expert educator.
        Generate 10 multiple-choice questions based on the user's topic.
        Include:
        - Question
        - Four options
        - Correct Answer
        - Short Explanation
        """,
    "Blanks":"""
        You are an expert educator.
        Generate 10 Fill in the Blanks questions based on the user's topic.
        Include:
        - Question
        - Correct Answer
        - Short Explanation
        """,
    "Short Answers":"""
        You are an expert educator.
        Generate 10 Short answer questions based on the user's topic.
        Include:
        - Question
        - Correct Answer
        - Short Explanation
        """,
    "True/False":"""
        You are an expert educator.
        Generate 10  True/False questions based on the user's topic.
        Include:
        - Question
        - Correct Answer
        - Short Explanation
        """
}

client=genai.Client(api_key=GEMINI_API_KEY)

def question_generator_assistant(question,question_form):
    system_promt=question_type[question_form]
    try:
        response=client.models.generate_content(
            model="gemini-3.5-flash",
            config=types.GenerateContentConfig(
                system_instruction=system_promt,
                temperature=0.4
                # max_output_tokens=2000
            ),
            contents=question
        )
        return response.text 
    except Exception:
        return ("Model is currently unavailable or busy. "
            "Please try again after a few moments.")


demo=gr.Interface(
    fn=question_generator_assistant,
    inputs=[
        gr.Textbox(lines=5,placeholder="Enter the Concept to generate questions",label="Text-Input"),
        gr.Radio(list(question_type.keys()),label="Question_type",value="MCQs")
    ],
    outputs=gr.Textbox(lines=7,label="Generated_questions"),
    title="Question Generator Assistant",
    description="Generate the Questions in different formats"
)

demo.launch(debug=True)

