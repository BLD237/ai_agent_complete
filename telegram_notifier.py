import requests
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
from urllib.parse import quote


def send_telegram_message(title, summary):
    message = summary  # Already formatted with Markdown
    url = (
        f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        f"?chat_id={TELEGRAM_CHAT_ID}"
        f"&text={quote(message)}"
        f"&parse_mode=Markdown"
    )
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print("Telegram API error:", response.text)
        return response.status_code == 200
    except Exception as e:
        print(f"Telegram error: {e}")
        return False