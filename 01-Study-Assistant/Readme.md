# 📖 Study Assistant

A simple AI-powered Study Assistant built using Python and Google's Gemini API.

## 🚀 Features

- Explains any topic in simple language
- Uses Gemini 2.5 Flash model
- Secure API key management using `.env`

## 🛠️ Tech Stack

- Python
- Google Gemini API (`google-genai`)
- python-dotenv

## 📂 Project Structure

```
01-Study-Assistant/
│── app.py
│── .env.example
│── requirements.txt
│── README.md
```

## ▶️ Run the Project

1. Install dependencies

```bash
pip install -r requirements.txt
```

2. Create a `.env` file

```text
GEMINI_API_KEY=your_api_key_here
```

3. Run

```bash
python app.py
```

## 📌 Example Prompt

```
Explain the topic 'Python' in two lines.
```