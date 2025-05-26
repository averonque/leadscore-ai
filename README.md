# Lead Capture AI Scoring System

## Overview
Captures lead data via form, scores with OpenAI, saves to SQLite, and simulates automation.

## Setup
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

Then open `frontend/index.html` in a browser.

## Features
- OpenAI scoring
- SQLite persistence
- Slack/email trigger simulation
