from fastapi import FastAPI
from backend.routers.auth import router as auth_router

app = FastAPI(
    title="MarketMind AI Backend"
)

app.include_router(auth_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to MarketMind AI Backend"
    }
from backend.routers.sales import router as sales_router
app.include_router(auth_router)
app.include_router(sales_router)