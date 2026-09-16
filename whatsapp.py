import httpx
from config import ACCESS_TOKEN, PHONE_NUMBER_ID

class WhatsappClient:

    BASE_URL = "https://graph.facebook.com/v25.0"

    def __init__(self):

        self.headers = {
            "Authorization": f"Bearer {ACCESS_TOKEN}",
            "content-type": "application/json"
        }

    async def send_text(self, to: str, text: str):

        url = f"{self.BASE_URL}/{PHONE_NUMBER_ID}/messages"

        payload = {
            "messaging_product": "whatsapp",
            "to": to,
            "type": "text",
            "text": {
                "body": text
            }
        }

        async with httpx.AsyncClient() as client:

            response = await client.post(
                url,
                headers = self.headers,
                json = payload
            )

        return response.json()