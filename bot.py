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
        bot_token="5815486417:AAHUHwtEc6NzPqLo8Pw1gVbud_SOTZVV9FA",
        api_id=int(15952578),
        api_hash="3600ce5f8f9b9e18cba0f318fa0e3600",
        plugins=plugins,
    )
    app.run()
