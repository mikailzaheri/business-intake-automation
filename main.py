from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .db import Base, engine, SessionLocal
from .models import IntakeRecord
from .schemas import IntakeRequest, IntakeResponse
from .services import classify_message, assign_urgency, generate_summary

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Business Intake Automation Demo")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Business Intake Automation Demo is running"}

@app.post("/intake", response_model=IntakeResponse)
def create_intake(payload: IntakeRequest, db: Session = Depends(get_db)):
    category = classify_message(payload.message)
    urgency = assign_urgency(payload.message)
    summary = generate_summary(payload.name, category, payload.message)

    record = IntakeRecord(
        name=payload.name,
        email=payload.email,
        phone=payload.phone,
        business_type=payload.business_type,
        message=payload.message,
        category=category,
        urgency=urgency,
        summary=summary,
    )

    db.add(record)
    db.commit()
    db.refresh(record)

    return IntakeResponse(
        status="success",
        category=category,
        urgency=urgency,
        summary=summary,
    )
