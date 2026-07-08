from sqlalchemy.orm import Session
from backend.models import User, Sale

def create_user(db: Session, name: str, email: str, password: str, role: str):
    user = User(
        name=name,
        email=email,
        password=password,
        role=role
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def create_sale(db: Session, sale):
    new_sale = Sale(
        customer_id=sale.customer_id,
        user_id=sale.user_id,
        sale_date=sale.sale_date,
        total_amount=sale.total_amount,
        payment_method=sale.payment_method,
        status=sale.status
    )

    db.add(new_sale)
    db.commit()
    db.refresh(new_sale)

    return new_sale


def get_all_sales(db: Session):
    return db.query(Sale).all()