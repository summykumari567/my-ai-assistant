🛍️ Meesho Support Chat API (FastAPI + OpenAI)

A simple customer support chatbot API built using **FastAPI** with rule-based responses and an **OpenAI fallback** for handling general queries.

This project simulates a Meesho-like customer support assistant that:
- Handles common policy questions (COD, return, delivery, payment)
- Uses OpenAI (`gpt-4o-mini`) for intelligent fallback responses

---

## 🚀 Features

- ✅ FastAPI backend
- ✅ Rule-based policy responses
- ✅ AI fallback using OpenAI API
- ✅ Simple REST endpoints
- ✅ Easy to deploy

---

## 📂 Project Structure


project-folder/
│
├── main.py
├── requirements.txt
└── README.md


---

## 🛠️ Installation

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd <your-project-folder>
2️⃣ Create Virtual Environment (Recommended)
python -m venv venv

Activate:

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate
3️⃣ Install Dependencies
pip install fastapi uvicorn openai

Or create requirements.txt:

fastapi
uvicorn
openai

Then install:

pip install -r requirements.txt
🔑 Set OpenAI API Key

Set your environment variable:

Windows (PowerShell)
setx OPENAI_API_KEY "your_api_key_here"
Mac/Linux
export OPENAI_API_KEY="your_api_key_here"

Restart your terminal after setting the key.

▶️ Run the Server
uvicorn main:app --reload

Server will start at:

http://127.0.0.1:8000
📡 API Endpoints
✅ Health Check

GET /

Response:

{
  "status": "ok"
}
💬 Chat Endpoint

POST /chat

Request Body:
{
  "message": "Is COD available?"
}
Example Response:
{
  "reply": "Yes, Cash on Delivery (COD) is available on selected products depending on seller and location."
}
🧠 How It Works
🔹 Rule-Based Logic

If the user message contains:

cod → COD policy response

return / exchange → Return policy response

delivery → Delivery timeline response

payment → Payment methods response

🔹 AI Fallback

If no keyword matches:

The message is sent to OpenAI

Model used: gpt-4o-mini

System prompt:
"You are a polite Meesho customer support agent."

📌 Example Test Using cURL
curl -X POST http://127.0.0.1:8000/chat \
-H "Content-Type: application/json" \
-d '{"message":"How can I track my order?"}'
📖 Swagger Documentation

After running the server, open:

http://127.0.0.1:8000/docs

Interactive API documentation powered by FastAPI.

🔮 Future Improvements

Add product database

Add order tracking integration

Add authentication

Add conversation memory

Deploy on Render / Railway / AWS

🏗️ Tech Stack

Python

FastAPI

Uvicorn

OpenAI API

📄 License

This project is for learning and demonstration purposes.


---

If you want, I can now:

- Make a **professional GitHub portfolio version**
- Add **Dockerfile**
- Add **Render deployment steps**
- Convert this into a strong resume-ready project description**