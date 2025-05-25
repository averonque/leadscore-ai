from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from database import SessionLocal
from models import Lead
from ai_scorer import score_lead
from dotenv import load_dotenv
from slack_notifier import send_slack_message



load_dotenv()


app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware, allow_origins=origins, allow_methods=["*"], allow_headers=["*"]
)

class LeadInput(BaseModel):
    name: str
    email: str
    company_size: str
    job_title: str
    website: str
    message: str

@app.post("/submit")
async def submit_lead(lead: LeadInput):
    score = await score_lead(lead.dict())
    print(score)
    db = SessionLocal()
    new_lead = Lead(**lead.dict(), score=score)
    db.add(new_lead)
    db.commit()
    db.close()
    if score == "High":
        print("🚀 Trigger Slack/Email Simulation: High quality lead!")
        await send_slack_message(lead.dict())
    return {"status": "success", "score": score}
