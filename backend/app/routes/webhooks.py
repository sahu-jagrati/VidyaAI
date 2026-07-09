from fastapi import APIRouter, Request, HTTPException, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.services import razorpay_service, subscription_service

router = APIRouter(prefix="/api/webhooks", tags=["webhooks"])


@router.post("/razorpay")
async def razorpay_webhook(request: Request, db: Session = Depends(get_db)):
    body = await request.body()
    signature = request.headers.get("x-razorpay-signature", "")

    if not razorpay_service.verify_webhook_signature(body, signature):
        raise HTTPException(status_code=400, detail="Invalid webhook signature")

    try:
        import json
        event = json.loads(body)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid JSON payload")

    subscription_service.handle_webhook_event(db, event)
    return {"status": "ok"}
