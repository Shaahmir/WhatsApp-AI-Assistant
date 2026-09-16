import os
from dotenv import load_dotenv

load_dotenv(override = True)

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")