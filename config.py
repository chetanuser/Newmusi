import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 10248430
API_HASH = "42396a6ff14a569b9d59931643897d0d"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "6618122929:AAH3_xWlXb8Ye_VfbY8CxcJBSULz_KFef2U"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://satreopalsen:pushkar@cluster0.vlkdddb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0" #getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 5400))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "5400")
)
# Chat id of a group for logging bot's activities
LOGGER_ID = -1001907436368

# Get this value from @Hot_Girl_Robot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "6203163206"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/chetanuser/Newmusi",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "SIGMA")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/SUKUNA_UPDATE_CHANNEL")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Shizuka_update_group")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "True")
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "500"))
# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5"))
# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @Venom_string_robot on Telegram
STRING1 = "BQFx4q8AJY8DnBnTExgT6HYfFHJMa2Xk3fMKvbNC3oGqRfaD9GNpM_6yGPYSt_G-0aIyMepMVu5pWxdv2wZjoSEXvNn1JozBWM8QBt8TEs-y_UUpl76iGI1XQuo7-9EzW6ePrjAy9jEtcuiwM847nhGKMQo-5d8RDiHfpwa7r-QCekbcLnRszHcWdUN5YP8PBy2j2Vl9b6BRSZTiE2UL4ZHP7fpNyAZJLanGQNtV6QAFMZGviLTC6qj3Z9eOxYh7y7EwMPXSJVMlT0wPdiwImhl_at8pL6YCgC71MUMI1793e9NUKt0d2oTRUXj8lXYcuB-6xvQKRwagYhr4KFiIj3vzF8jVnQAAAAFPrvAtAA" #"BQCcYO4AOC7NPimTcvq7T6XfIiwMQxh9Z6XKRcV8ybMTiZXznqnOdfzpvAYQbCNsCOfWz31wR6pAjGecCP3nojlZOnaqUpbvDXuhQbHLgY9iHn_ikwbuZkUaOAWzBEnair1nZUzONb62bBgFR7XwhVVYhmkWxSHWfvBM6hALc-PkrT5SGBwL5Fz_XcXii5tHzB3UVw5ASkL2YXz9sCh5N2PdOAH8eOjPrWb5NL5wagRBm9kIcAbCIeED725GMCfGRmdvzbdYv9TiS_Q65Qp31KkXVST1Yov07cSd_c6Mh5ATG1t5zX3Ift43lu3-GS9vO0qLW0XZPnpH1ZOaQFFyo8sHXgra6wAAAAFyF4XTAA" #getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/407b7c3930c1158f1492f.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/407b7c3930c1158f1492f.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/9bdd7cda2738dbd5c2505.jpg"
STATS_IMG_URL = "https://graph.org/file/407b7c3930c1158f1492f.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/9eb6d3372d5880d1ed4a2.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/d36a494d662d8b9f350d0.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/8f8ea633467c2a78d3d9a.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/a9ed7db13cf412221ae01.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/28ed330e5d17c7ad9bb30.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/9bdd7cda2738dbd5c2505.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/ee3492526f6a45c2672a0.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/28ed330e5d17c7ad9bb30.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
