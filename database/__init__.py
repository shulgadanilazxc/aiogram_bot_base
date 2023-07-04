from tortoise import Tortoise
from data import POSTGRES_URI

async def initialize():
    await Tortoise.init(
        db_url=POSTGRES_URI,
        modules={"models": ["database.models"]},
    )
    await Tortoise.generate_schemas()
