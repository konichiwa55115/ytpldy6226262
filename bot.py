import logging

logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

import pyrogram, os

if __name__ == "__main__":
    plugins = dict(root="plugins")
    app = pyrogram.Client(
        "bot",
        bot_token="5936802228:AAFwW7cZlF8waTYTyVe8m3nUYhJg5EF9Eso",
        api_id=int(17983098),
        api_hash="ee28199396e0925f1f44d945ac174f64",
        plugins=plugins,
    )
    app.run()
