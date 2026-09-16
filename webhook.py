import asyncio
from ai import call_llm

from fastapi import APIRouter, Request
from fastapi.responses import PlainTextResponse
from config import VERIFY_TOKEN
from whatsapp import WhatsappClient

wa = WhatsappClient()
router = APIRouter()

@router.get("/webhook")
async def verify_webhook(request: Request):

    mode = request.query_params.get("hub.mode")
    token = request.query_params.get("hub.verify_token")
    challenge = request.query_params.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return PlainTextResponse(challenge)

    return PlainTextResponse(
        "Verification failed",
        status_code = 403
    )

@router.post("/webhook")
async def receive_message(request: Request):

    body = await request.json()
    print(body)

    try:
        message = body["entry"][0]["changes"][0]["value"]["messages"][0]
        sender = message["from"]
        text = message["text"]["body"]
        message_id = message["id"]

        reply = await asyncio.to_thread(call_llm, text)

        await wa.send_text(
            to = sender,
            text = reply
        )

    except Exception as e:
        print("ERROR:", e)
        print(body)

    return {
        "status": "ok"
    }