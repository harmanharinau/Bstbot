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
    ABOUT_BOT_TEXT = """<b>This is Bst Market Bot.

ð¤ My Name: <a href='https://t.me/cyniteofficial'>Bst Market Bot</a>

ð Language : <a href='https://www.python.org'> Python V3</a>

ð Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

ð¡ Server: <a href='https://heroku.com'>Heroku</a>

ð¨âð» Created By: <a href='https://t.me/clashuser'>Cynite</a></b>
"""

    ABOUT_HELP_TEXT = """<b>ð¨âð» Developer : <a href='https://t.me/clashuser'>Click Me</a>

If You Want Access To This Bot And Want To Add Your Own Clans/Accounts On Sell Free Then Contact The Developer.</b>
"""

    HOME_TEXT = """
<b>Hey! {}ð,

I'm Bst Market Robot.ð¤</a>

I Can Search ð Clan/Accounts For Youâ

<a>Made With â¤ By @Clashuser</a></b>
"""


    START_MSG = """
<b>Hey! {}ð,

I'm Bst Market Robot.ð¤</a>

I Can Search ð Clan/Accounts For Youâ

<a>Made With â¤ By @Clashuser</a></b>
"""


