from pydantic import BaseModel, Field
from typing import Literal

class WalletEntity(BaseModel):
    uuid: str
    balance: int

class WalletUpdate(BaseModel):
    amount: int | float = Field(gt=0)
    operation_type: Literal["DEPOSIT", "WITHDRAW"]
