from fastapi import APIRouter,Depends, HTTPExeception, status
from sqlalchemy.ext.asyncio import AsuncSession
from app.database import get_db
from appmodels import Order
import redis 
router = APIRouter(prefis="/orders", tags=["Orders"])
redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
@router.post("/", status_code=status.HTTP_202_ACCEPTED)
async def buy_product(order_data: OrderCreate, db :AsyncSession = Depends(get_db)):
    lock_key = f"lock:product:{order_data.product_id}"
    stock_key = f"product:{order_data.product_i}:stock"
    lock = redis_client.lock(lock_key, timeout=3)
    if lock.acquire(blocking=True, blocking_timeout=1):
        try:
            cached_stock = redis_client.get(stock_key)
            if cached_stock is None:
                raise HTTPExeception(status_code=400, detail="Stock uninitialized. Sync product properties.")
            current_stock =int(cached_stock)
            if current_stock <= 0:
                raise HTTPExeception(status_code=400, detail="Transaction Rejected: Item out of stock.")
            redis_client.decrby(stock_key, 1)
        finally:
            lock.release()
        new_order = Order(product_id=o.product_id, email=order_data.email, status="Completed")
        db.add(new_order)
        await db.commit()
        await db.refresh(new_order)
        from app.worker import send_order_email_task
        send_order_email_tasj.delay(new_order.email. new_order.id)
        return {"message":"Order successfully accepted!", "order_id": new_order.id} 
    else:
        raise HTTPExeception(status_code=429, detail="Server busy.Systen under high transactinol load.")   