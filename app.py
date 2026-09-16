from fastapi import FastAPI
from whatsapp import WhatsappClient
from webhook import router

app = FastAPI()
app.include_router(router)
wa = WhatsappClient()

@app.get("/")
async def home():
    return {
        "status": "Running Fine!"
    }

@app.get("/send")
async def send():

    response = await wa.send_text(
        to = "923174841070",
        text = "Hello from Shahmir!"
    )

    return response