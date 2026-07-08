from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import bcrypt

from backend.database import get_db
from backend.schemas import UserCreate, UserLogin
from backend.crud import create_user, get_user_by_email
from backend.security import create_access_token

router = APIRouter()


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = bcrypt.hashpw(
        user.password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")

    new_user = create_user(
        db=db,
        name=user.name,
        email=user.email,
        password=hashed_password,
        role=user.role
    )

    return {
        "message": "User Registered Successfully",
        "id": new_user.id
    }


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    db_user = get_user_by_email(db, user.email)

    if db_user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid Email"
        )

    if not bcrypt.checkpw(
        user.password.encode("utf-8"),
        db_user.password.encode("utf-8")
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid Password"
        )

    access_token = create_access_token(
        data={
            "sub": db_user.email,
            "role": db_user.role
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": db_user.name,
        "role": db_user.role
    }