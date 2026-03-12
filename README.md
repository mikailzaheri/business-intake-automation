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

