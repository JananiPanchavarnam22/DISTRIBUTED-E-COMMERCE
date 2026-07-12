from pydantic import BaseModel, EmailStr, Field
class OrderCreate(BaseModel):
    product_id:int = Fiel d(...,gt=0)
    email: EmailStr
class OrderResponse(BaseModel):
    id: int
    product_id: int
    email: str
    status: str
    class Config:
        from_attributes=True