from data import POSTGRES_URI

TORTOISE_ORM = {
    "connections": {"default": POSTGRES_URI},
    "apps": {
        "models": {
            "models": ["database.models"],
            "default_connection": "default",
        },
    },
}
