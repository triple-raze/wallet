import asyncpg
from dotenv import load_dotenv
from os import getenv

load_dotenv()    # переменные окружения

async def execsql(query: str, args: tuple = (), first=False):

    pool = await asyncpg.create_pool(
        database = getenv('ENV_POSTGRES_DB'),
        user = getenv('ENV_POSTGRES_USER'),
        password = getenv('ENV_POSTGRES_PASSWORD'),
        port = getenv('ENV_POSTGRES_PORT')          
    )
    
    async with pool.acquire() as conn:
        result = await conn.fetch(query, *args)

    await pool.close()

    if not result:
        return None

    if first:
        return result[0]

    return result

