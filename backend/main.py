import os
from fastapi import FastAPI, Request
from openai import OpenAI

app = FastAPI()

client = OpenAI()  # Uses OPENAI_API_KEY automatically

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/chat")
async def chat(req: Request):
    data = await req.json()
    user_msg = data.get("message", "").lower()

    # ---------- MEESHO POLICY LOGIC ----------
    if "cod" in user_msg:
        return {"reply": "Yes, Cash on Delivery (COD) is available on selected products depending on seller and location."}

    if "return" in user_msg or "exchange" in user_msg:
        return {"reply": "You can return or exchange products within 7 days of delivery, subject to seller policy."}

    if "delivery" in user_msg:
        return {"reply": "Orders are usually delivered within 5–10 business days depending on seller and location."}

    if "payment" in user_msg:
        return {"reply": "We support UPI, Debit Card, Credit Card, Net Banking, and COD on eligible products."}

    # ---------- AI FALLBACK ----------
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a polite Meesho customer support agent."},
            {"role": "user", "content": user_msg}
        ]
    )

    return {"reply": response.choices[0].message.content}
















