from models.wallet import WalletUpdate
from db import crud

from fastapi import APIRouter 
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/{uuid}/operation")
async def wallet_operation(data: WalletUpdate, uuid: str):
    operation_type = data.operation_type
    amount = data.amount

    wallet = await crud.get_wallet(uuid)
    
    if not wallet:
        return JSONResponse({"detail": "Wallet not found"}, status_code=404)

    balance = wallet['balance']

    if operation_type == "DEPOSIT":
        updated_wallet = await crud.update_wallet(uuid, balance + amount)
    
    elif operation_type == "WITHDRAW":
        updated_wallet = await crud.update_wallet(uuid, balance - amount)

    return JSONResponse({
        "uuid": uuid,
        "balance": updated_wallet['balance']
    }, status_code=200)


@router.post("/create")
async def create_wallet():
    wallet = await crud.create_wallet()
    uuid = wallet['uuid']

    return JSONResponse({"uuid": uuid}, status_code=201)


@router.get("/{uuid}")
async def get_wallet(uuid: str):
    wallet = await crud.get_wallet(uuid)
    
    if not wallet:
        return JSONResponse({"detail": "Wrong wallet uuid"}, status_code=404)
    
    return JSONResponse({
        "uuid": uuid,
        "balance": wallet['balance']
    }, status_code=200)

