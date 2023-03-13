import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "27329085"))
API_HASH = getenv("API_HASH", "0fb41ad125032deac1578a599aefec48")

BOT_TOKEN = getenv("BOT_TOKEN", "5939839321:AAFiixf8BPkpv8JTDODbBqEv5wOfCABt1Ds")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Aman:Aman@cluster0.gt2bc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001861990174"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "ℭ𝔩𝔲𝔟 𝔪𝔲𝔰𝔦𝔠")

OWNER_ID = list(map(int, getenv("OWNER_ID", "6194191308").split()))

HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/AnonymousX1025/AnonXMusic")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/TEAM_XTRON")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/welcomehfc")

SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "180"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "12"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", "BQHIQ4IAQH_Az4BMTezoGJ2HSCXJ9UZK5IafFrPjgJfgvO5QgnFkU3Q0nf6SAC7vhwLhqJ7B0OSk0OdteS-2YUEpFbEjGHG-Xtu4xPwAIDm6_hosyEltql6JH25mXN2XyK98jfI3OtYQ7KJJ2LuQnXsVBdUU6POubovEmSo0H6qBhJ8xnRqPPQk4yleOgnIuXjNEn-9dVBbuUBvS1XwBpqT7vMCum2Rlfge6ysbuOLOf8bdY1DLFFBcQjjZmItph3Q8nptsR_XWyZMhQGwOP7OdMylXUwsmgzQtpCj_N58UQuiR9uQsmQNE8qNUTEfxZMLpSmF47g-bg9cBE5XpCs6M-1B-rMgAAAAFxKDMVAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []


START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/74751f394c00f9cfea9bc.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://telegra.ph/file/74751f394c00f9cfea9bc.jpg",
)

PLAYLIST_IMG_URL = "https://telegra.ph/file/74751f394c00f9cfea9bc.jpg"

GLOBAL_IMG_URL = "https://telegra.ph/file/74751f394c00f9cfea9bc.jpg"

STATS_IMG_URL = "https://telegra.ph/file/74751f394c00f9cfea9bc.jpg"

TELEGRAM_AUDIO_URL = "https://telegra.ph/file/74751f394c00f9cfea9bc.jpg"

TELEGRAM_VIDEO_URL = "https://telegra.ph/file/74751f394c00f9cfea9bc.jpg"

STREAM_IMG_URL = "https://telegra.ph/file/74751f394c00f9cfea9bc.jpg"

SOUNCLOUD_IMG_URL = "https://telegra.ph/file/74751f394c00f9cfea9bc.jpg"

YOUTUBE_IMG_URL = "https://telegra.ph/file/74751f394c00f9cfea9bc.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/74751f394c00f9cfea9bc.jpg"

SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/74751f394c00f9cfea9bc.jpg"

SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/74751f394c00f9cfea9bc.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)


if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            PING_IMG_URL = "https://telegra.ph/file/74751f394c00f9cfea9bc.jpg"

if START_IMG_URL:
    if START_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://telegra.ph/file/74751f394c00f9cfea9bc.jpg"
