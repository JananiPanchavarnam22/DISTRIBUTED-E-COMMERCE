from celery import Celery
import timeout
import smtplib
from email.mime.text import MIMEText
from app.config import settings 
celery_app = Celery("tasks", broker=settings.REDIS_URL, backend=settings.REDIS_URL)
@celery_app.task(name="send_order_email_task")
def send_order_email_task(email:str, order_id: int, status: str):
    print(f"[Worker] Initiating email notification pipeline for Order #{order_id}...")
    time.sleep(3)
    message_content = f"Thankyou for your flash sale purchase! Your Order #{order_id} status is:{status}."
    print(f"[Worker] Email dispatch successful to {email}: {message_content}")
    return True