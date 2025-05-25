from openai import OpenAI
from dotenv import load_dotenv

import os


load_dotenv()

OPENAI_KEY = os.getenv("OPENAI_KEY")

client = OpenAI(
  api_key=OPENAI_KEY
)


def extract_score(text):
    for line in text.splitlines():
        if line.lower().startswith("score:"):
            return line.split(":", 1)[1].strip()




async def score_lead(data):
    prompt = f"""
    Based on the following lead data:
    Name: {data['name']}
    Email: {data['email']}
    Company Size: {data['company_size']}
    Job Title: {data['job_title']}
    Website: {data['website']}
    Message: {data['message']}
    Provide answer in this Format:
    Score: classify it as High, Medium, or Low quality
    Explanation: 
    """
    try:
        

        completion = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        messages=[
            {"role": "user", "content": prompt}
        ]
        )
       
        score = extract_score(completion.choices[0].message.content.strip())

        return score
    except Exception as e:
        print("⚠️ AI Scoring Failed:", e)
        return "Medium"
