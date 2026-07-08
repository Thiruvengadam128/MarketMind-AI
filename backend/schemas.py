from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    role: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class SaleCreate(BaseModel):
    customer_id: int
    user_id: int
    sale_date: str
    total_amount: int
    payment_method: str
    status: str