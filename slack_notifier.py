import httpx
import os

# Replace this with your actual Slack webhook URL or set it as an environment variable
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

async def send_slack_message(lead):
    message = (
        f"🚀 *New High-Quality Lead!*\n"
        f"*Name:* {lead['name']}\n"
        f"*Email:* {lead['email']}\n"
        f"*Job Title:* {lead['job_title']}\n"
        f"*Company Size:* {lead['company_size']}\n"
        f"*Website:* {lead['website']}\n"
        f"*Message:* {lead['message']}"
    )
    async with httpx.AsyncClient() as client:
        response = await client.post(
            SLACK_WEBHOOK_URL,
            json={"text": message},
        )
        if response.status_code != 200:
            print(f"❌ Failed to send to Slack: {response.text}")
