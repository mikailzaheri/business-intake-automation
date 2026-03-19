![Python](https://img.shields.io/badge/python-3.10-blue)
![FastAPI](https://img.shields.io/badge/framework-fastapi-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

# Business Intake Automation Demo

A simple workflow automation backend that simulates how businesses can automate client intake, categorize requests, assign urgency, and prepare structured summaries for internal follow-up systems.

This project demonstrates how repetitive administrative workflows can be partially automated using lightweight backend services.

---

## Overview

Many businesses receive new inquiries through email or web forms. Staff then manually read the message, determine the type of request, decide priority, and log the information for follow-up.

This demo shows how that process can be automated.

The system:

1. Receives a client inquiry
2. Classifies the type of request
3. Assigns an urgency level
4. Generates an internal summary
5. Stores the record for further processing

---

## Example Business Use Cases

This workflow can apply to many industries:

**Law Firms**
- consultation requests
- document drafting inquiries
- legal service intake

**Accounting Firms**
- new client inquiries
- tax preparation requests
- bookkeeping questions

**Medical / Dental Clinics**
- appointment requests
- patient intake forms
- consultation inquiries

**Property Management**
- tenant maintenance requests
- rental inquiries
- service coordination

---

## Example Workflow

Manual Process:
Client sends email or form submission ↓ Staff reads message ↓ Staff categorizes request ↓ Staff logs information ↓ Staff follows up

Automated Workflow:
Client submits inquiry ↓ Automation service receives request ↓ Message is categorized ↓ Urgency is assigned ↓ Summary is generated ↓ Record stored in database ↓ Data ready for CRM / follow-up automation

---

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic

FastAPI provides a simple REST API with automatic interactive documentation.

---

## Project Structure
business-intake-automation/ │ ├── app/ │   ├── main.py │   ├── db.py │   ├── models.py │   ├── schemas.py │   ├── services.py │   └── utils.py │ ├── data/ │   └── intake.db │ ├── requirements.txt └── README.md

---

## Installation

Clone the repository:
git clone https://github.com/mikailzaheri/business-intake-automation.git cd business-intake-automation

Install dependencies:
pip install -r requirements.txt

Run the server:
uvicorn app.main:app --reload

Server will start at:
http://127.0.0.1:8000

---

## API Documentation

FastAPI automatically provides interactive API documentation.

Open:
http://127.0.0.1:8000/docs

You can test the API directly from this interface.

---

## Example Request

POST `/intake`
{ "name": "John Smith", "email": "john@example.com", "phone": "6041234567", "business_type": "law_firm", "message": "I need help drafting a commercial lease agreement." }

---

## Example Response
{ "status": "success", "category": "legal_document_request", "urgency": "medium", "summary": "New intake from John Smith regarding lease agreement drafting." }

---

## How Categorization Works

The system performs simple rule-based classification to determine the request category.

Examples:

| Keyword | Category |
|-------|---------|
| contract, lease, agreement | legal document request |
| appointment, consultation | scheduling request |
| invoice, billing, payment | billing request |

Urgency is also assigned based on keywords such as:

- urgent
- asap
- immediately
- soon

---

## Potential Extensions

This demo is intentionally simple, but can easily be extended with:

- CRM integration (HubSpot, Salesforce)
- Email notifications
- OpenAI / LLM summarization
- Webhook delivery
- Admin dashboard
- Task assignment automation
- Slack notifications
- Automated document generation

---

## Purpose of This Project

This repository demonstrates how simple backend automation services can reduce repetitive administrative work inside business operations.

Rather than replacing existing tools, automation systems typically connect to the tools a business already uses and streamline manual processes.

---

## License

MIT License
