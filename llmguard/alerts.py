import logging, os, requests
logger = logging.getLogger(__name__)

def send_slack_alert(payload: dict) -> None:
    url = os.getenv("SLACK_WEBHOOK_URL")
    if not url: return
    try: requests.post(url, json=payload, timeout=5)
    except Exception as e: logger.error(f"Slack fail: {e}")

def alert_killswitch_triggered(user_id: str, burn_rate: float, limit: float):
    send_slack_alert({"text": f"🚨 *Killswitch*\nUser: `{user_id}`\nBurn: `${burn_rate}/min`"})

def alert_daily_budget_exceeded(user_id: str, spent: float, limit: float):
    send_slack_alert({"text": f"💸 *Daily Budget*\nUser: `{user_id}`\nSpent: `${spent}`"})