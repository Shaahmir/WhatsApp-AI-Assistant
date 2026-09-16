# WhatsApp AI Assistant

An intelligent, RAG-powered WhatsApp AI assistant built with FastAPI and LLM APIs. Designed specifically to deliver context-aware, domain-specific insurance support for InsureLLM clients.

---

## Key Features

* **Retrieval-Augmented Generation (RAG):** Integrates vector stores to query InsureLLM policy documents and database records for grounded answers.
* **WhatsApp Cloud API Integration:** Handles real-time incoming messages, multi-turn user conversations, and status verification via webhooks.
* **Low-Latency Async Backend:** Built with FastAPI and Uvicorn for asynchronous message routing and fast response times.
* **Domain Guardrails:** Restricts model queries strictly to insurance coverage, contract terms, company policies, and support services.

---

## Tech Stack

| Component | Technology |
| --- | --- |
| **Language** | Python 3.11+ |
| **Backend Framework** | FastAPI, Uvicorn |
| **Package Manager** | uv / pip |
| **Vector Database** | ChromaDB (`Vector_DB`) |
| **LLM & Embeddings** | OpenAI API / NVIDIA NIM / Custom LLM |
| **Messaging Platform** | Meta WhatsApp Cloud API |

---

## Getting Started

### Prerequisites

* Python 3.11 or higher
* `uv` package manager (recommended) or standard `pip`
* Meta Developer Account with WhatsApp Cloud API access
* API key for your preferred LLM provider

### Installation

1. Clone the repository:
```bash
git clone https://github.com/shaahmir/WhatsApp-AI-Assistant.git
cd WhatsApp-AI-Assistant

```


2. Set up the virtual environment and install dependencies:
Using `uv`:
```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv sync

```


Using `pip`:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt

```



---

## Environment Configuration

1. Create a `.env` file from the template:
```bash
cp .env.example .env

```


2. Add your credentials to `.env`:
```env
# WhatsApp Cloud API Configuration
PHONE_NUMBER_ID=YOUR_PHONE_NUMBER_ID
ACCESS_TOKEN=YOUR_ACCESS_TOKEN
VERIFY_TOKEN=YOUR_VERIFY_TOKEN

PHONE_NUMBER=YOUR_PHONE_NUMBER
WHATSAPP_BUSINESS_ACCOUNT_ID=YOUR_WA_BUSINESS_ACC

# LLM Provider Configurations 
BASE_URL=LLM_PROVIDER_URL
API_KEY=YOUR_API_KEY

```

---

## Usage

1. Start the FastAPI server:
```bash
uvicorn app:app --reload --port 8000

```


2. Expose the local server for development:
```bash
ngrok http 8000

```


3. Configure Webhook:
* Go to the Meta Developer Portal under WhatsApp Webhook Settings.
* Set Callback URL to `https://<your-ngrok-domain>/webhook`.
* Provide the `VERIFY_TOKEN` defined in your `.env`.
* Subscribe to the `messages` event.



---

## Project Structure

```text
.
├── Vector_DB/        # Vector database index and persistent storage
├── .env.example      # Environment variable template
├── ai.py             # RAG pipeline logic and LLM prompt processing
├── app.py            # FastAPI entry point and web server routes
├── config.py         # App configuration, guardrails, and environment variables
├── webhook.py        # Webhook authorization and event processing
└── whatsapp.py       # Messaging client for sending WhatsApp payloads

```

---

## License

This project is licensed under the MIT License.
