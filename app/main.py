from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.routes import orders
app = FastAPI(title="Distributed E-commerece Engine Framework")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(orders.router)
@app.on_event("startup")
async def startup_event():
    async with engine.begin( )as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Architecture Booted Successfully.Structural Mappins Inintialized.")
