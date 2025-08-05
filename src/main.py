from routers.wallet_router import router as wallet_router

from fastapi import FastAPI

app = FastAPI(root_path="/api/v1")

app.include_router(wallet_router, prefix="/wallet")


