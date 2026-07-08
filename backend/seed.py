from backend.database import SessionLocal
from backend.models import (
    Role,
    User,
    Customer,
    Product,
    Inventory,
    Sale,
    SaleItem
)

import bcrypt
db = SessionLocal()

roles = [
    Role(role_name="Business Owner"),
    Role(role_name="Store Manager"),
    Role(role_name="Sales Executive"),
    Role(role_name="System Administrator")
]

db.add_all(roles)
db.commit()

password = bcrypt.hashpw(
    "admin123".encode("utf-8"),
    bcrypt.gensalt()
).decode("utf-8")

user = User(
    name="Admin",
    email="admin@gmail.com",
    password=password,
    role="Business Owner"
)

db.add(user)
db.commit()

customer = Customer(
    name="Ramesh",
    phone="9876543210",
    email="ramesh@gmail.com",
    address="Chennai"
)

db.add(customer)
db.commit()

product = Product(
    product_name="Laptop",
    category="Electronics",
    price=50000,
    cost_price=42000,
    description="Dell Laptop"
)

db.add(product)
db.commit()

inventory = Inventory(
    product_id=1,
    stock_quantity=20,
    minimum_stock=5,
    warehouse="Warehouse A"
)

db.add(inventory)
db.commit()

sale = Sale(
    customer_id=1,
    user_id=1,
    sale_date="2026-07-08",
    total_amount=50000,
    payment_method="UPI",
    status="Completed"
)

db.add(sale)
db.commit()

sale_item = SaleItem(
    sale_id=1,
    product_id=1,
    quantity=1,
    unit_price=50000,
    subtotal=50000
)

db.add(sale_item)
db.commit()

db.close()

print("Sample data inserted successfully!")