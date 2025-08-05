"""db init

Revision ID: 1e04ffe52105
Revises: 
Create Date: 2025-08-04 04:54:34.951858

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1e04ffe52105'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""CREATE TABLE wallets (
	uuid VARCHAR(36) PRIMARY KEY NOT NULL,
	balance BIGINT DEFAULT 0 NOT NULL
    )""")



def downgrade() -> None:
    op.execute("""DROP TABLE wallets""")

