# (c) @RoyalKrrishna

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "MdiskSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    BOT_OWNER = int(os.environ.get("BOT_OWNER"))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b>This is Mdisk Search Bot.

🤖 My Name: <a href='https://t.me/cyniteofficial'>Bst Market Bot</a>

📝 Language : <a href='https://www.python.org'> Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

📡 Server: <a href='https://heroku.com'>Heroku</a>

👨‍💻 Created By: <a href='https://t.me/clashuser'>Cynite</a></b>
"""

    ABOUT_HELP_TEXT = """<b>👨‍💻 Developer : <a href='https://t.me/clashuser'>Click Me</a>

If You Want Access To This Bot And Want To Add Your Own Clans/Accounts On Sell Free Then Contact The Developer.</b>
"""

    HOME_TEXT = """
<b>Hey! {}😅,

I'm Bst Market Robot.🤖</a>

I Can Search 🔍 Clan/Accounts For You❗

<a>Made With ❤ By @Clashuser</a></b>
"""


    START_MSG = """
<b>Hey! {}😅,

I'm Bst Market Robot.🤖</a>

I Can Search 🔍 Clan/Accounts For You❗

<a>Made With ❤ By @Clashuser</a></b>
"""


