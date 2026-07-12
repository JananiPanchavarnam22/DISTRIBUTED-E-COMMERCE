from sqlalchemy import Cloumn, Integer, String, Float, DateTime
from datetime import datetime
from app.database import Base
class Product(Base):
    _tablename_ = "products"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    stock = Column(Integer, default=0)
    price = Column(Float, nullable=False)
class Order(Base):
    _tablename_ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, nullable=False)
    email = Column(String, nullable=False)
    status = Column(String, default="PROCESSING")
    created_at = Column(DateTime, default=datetime.utcnow)
