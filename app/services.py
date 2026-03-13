def classify_message(message: str) -> str:
    text = message.lower()

    if "contract" in text or "agreement" in text or "lease" in text:
        return "legal_document_request"
    if "appointment" in text or "schedule" in text or "consultation" in text:
        return "scheduling_request"
    if "invoice" in text or "payment" in text or "bill" in text:
        return "billing_request"
    return "general_inquiry"

def assign_urgency(message: str) -> str:
    text = message.lower()

    if "urgent" in text or "asap" in text or "immediately" in text:
        return "high"
    if "soon" in text or "this week" in text:
        return "medium"
    return "low"

def generate_summary(name: str, category: str, message: str) -> str:
    short_message = message.strip()
    if len(short_message) > 120:
        short_message = short_message[:117] + "..."
    return f"New intake from {name}. Category: {category}. Message: {short_message}"
