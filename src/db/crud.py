from db.connection import execsql
from models.wallet import WalletEntity, WalletUpdate

from uuid import uuid4

async def create_wallet() -> WalletEntity:
    uuid = str(uuid4())
    return await execsql("INSERT INTO wallets VALUES ($1) RETURNING *", (uuid,), first=True)


async def get_wallet(uuid: str) -> WalletEntity:
    wallet = await execsql("SELECT * FROM wallets WHERE uuid = $1", (uuid,), first=True)
    return wallet

async def update_wallet(uuid: str, balance: int) -> None:
    return await execsql(
        "UPDATE wallets SET balance = $2 WHERE uuid = $1 " \
        "RETURNING *", (uuid, balance), first=True)

async def delete_wallet(uuid: str) -> None:
    await execsql("DELETE FROM wallets WHERE uuid=$1", (uuid,))

