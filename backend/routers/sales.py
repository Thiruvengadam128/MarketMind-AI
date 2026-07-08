from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.schemas import SaleCreate
from backend.crud import create_sale, get_all_sales

router = APIRouter()


@router.post("/sales")
def upload_sales(
    sale: SaleCreate,
    db: Session = Depends(get_db)
):
    new_sale = create_sale(db, sale)

    return {
        "message": "Sales data uploaded successfully",
        "sale_id": new_sale.id
    }


@router.get("/sales")
def fetch_sales(db: Session = Depends(get_db)):
    sales = get_all_sales(db)
    return sales