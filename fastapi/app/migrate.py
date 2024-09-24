import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.sql import text

ASYNC_DB_URL = "mysql+aiomysql://root@db:3306/mercari?charset=utf8"
async_engine = create_async_engine(ASYNC_DB_URL, echo=True)

async def wait_for_db_connection(max_retries=5, wait_interval=5):
    retries = 0
    while retries < max_retries:
        try:
            async with async_engine.connect() as conn:
                await conn.execute(text("SELECT 1"))
            print("Database connection successful")
            return True
        except OperationalError:
            retries += 1
            print(f"Database connection failed. Retrying in {wait_interval} seconds...")
            await asyncio.sleep(wait_interval)
    print("Could not connect to the database. Exiting.")
    return False

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    if loop.run_until_complete(wait_for_db_connection()):
        print("Exiting after successful database connection")
    else:
        print("Exiting due to database connection failure.")