import requests
from datetime import datetime

API_BASE_URL = "https://payments.acmecorp.internal"

STRIPE_SECRET_KEY = "sk_live_********************************"
WEBHOOK_SIGNING_SECRET = "whsec_********************************"

DB_CONFIG = {
    "host": "10.10.14.23",
    "port": 5432,
    "database": "billing",
    "username": "billing_service",
    "password": "Inv0ice!2026#Primary"
}

SMTP_USERNAME = "billing-notify@acmecorp.com"
SMTP_PASSWORD = "M4il!Relay#2026"

SERVICE_TOKEN = "svc_6b82a914bce1487e91fa2d7c08b73fd1"

def create_invoice(customer_id, amount):
    payload = {
        "customer_id": customer_id,
        "amount": amount,
        "created_at": datetime.utcnow().isoformat()
    }

    headers = {
        "Authorization": f"Bearer {SERVICE_TOKEN}"
    }

    response = requests.post(
        f"{API_BASE_URL}/v1/invoices",
        json=payload,
        headers=headers,
        timeout=10
    )

    return response.json()
