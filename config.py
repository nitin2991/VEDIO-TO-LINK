from operator import add
import os
import logging
from logging.handlers import RotatingFileHandler

# No need to load dotenv if you want hardcoding
# If you want dotenv support, uncomment below lines
# import dotenv
# dotenv.load_dotenv()

# Bot Configuration

# Force user to join channels
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002119118222"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002197765596"))

if FORCE_SUB_CHANNEL > FORCE_SUB_CHANNEL2:
    temp = FORCE_SUB_CHANNEL2
    FORCE_SUB_CHANNEL2 = FORCE_SUB_CHANNEL
    FORCE_SUB_CHANNEL = temp

# Bot token from BotFather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8172817242:AAFuLyeYiWLTyUuFRF_sMUs2jvCZGMquQMA")

# API credentials from https://my.telegram.org/apps
APP_ID = int(os.environ.get("APP_ID", "29801489"))
API_HASH = os.environ.get("API_HASH", "74aaff69f6cacf1239d6a6f38a24374c")

# Channel where files will be saved
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002268736665"))

# Bot owner ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6667276878"))

# MongoDB Database URL and Name
DB_URL = os.environ.get("DB_URL", "mongodb+srv://nitin:nitin000001@sharebot.tcyjilw.mongodb.net/?retryWrites=true&w=majority&appName=sharebot")
DB_NAME = os.environ.get("DB_NAME", "nitin")

# Port for deployment (default 6245)
PORT = int(os.environ.get("PORT", "6245"))

# Bot Messages
BOT_STATS_TEXT = os.environ.get("BOTS_STATS_TEXT", "<b>𝙱𝙾𝚃 𝚄𝙿𝚃𝙸𝙼𝙴 </b>\n{uptime}")
USER_REPLY_TEXT = os.environ.get("USER_REPLY_TEXT", "❌ 𝙿𝚕𝚎𝚊𝚜𝚎 𝙰𝚟𝚘𝚒𝚍 𝙳𝚒𝚛𝚎𝚌𝚝 𝙼𝚎𝚜𝚜𝚊𝚐𝚎𝚜. 𝙸'𝚖 𝚆𝚘𝚛𝚔𝚒𝚗𝚐 𝙵𝚘𝚛 𝙾𝚗𝚕𝚢  @Nitin_510")
START_MSG = os.environ.get("START_MESSAGE", "𝙷𝚎𝚕𝚕𝚘 {first}\n\n𝙸 𝙲𝚊𝚗 𝚂𝚝𝚘𝚛𝚎 𝙿𝚛𝚒𝚟𝚊𝚝𝚎 𝙵𝚒𝚕𝚎𝚜 𝚒𝚗 𝚂𝚙𝚎𝚌𝚒𝚏𝚒𝚎𝚍 𝙲𝚑𝚊𝚗𝚗𝚎𝚕 𝚊𝚗𝚍 𝚘𝚝𝚑𝚎𝚛 𝚞𝚜𝚎𝚛𝚜 𝚌𝚊𝚗 𝚊𝚌𝚌𝚎𝚜𝚜 𝙿𝚛𝚒𝚟𝚊𝚝𝚎 𝙵𝚒𝚕𝚎𝚜 𝙵𝚛𝚘𝚖 𝚊 𝚂𝚙𝚎𝚌𝚒𝚊𝚕 𝙻𝚒𝚗𝚔....!\n\n𝙿𝚘𝚠𝚎𝚛𝚎𝚍 𝙱𝚢 @Nitin_510 🔥")
OWNER_TAG = os.environ.get("OWNER_TAG", "Nitin_510")

# Delete message after some time
TIME = int(os.environ.get("TIME", "1800"))

# Shortener Settings
USE_SHORTLINK = True if os.environ.get('USE_SHORTLINK', "TRUE") == "TRUE" else False
SHORTLINK_API_URL = os.environ.get("SHORTLINK_API_URL", "urlwala.com")
SHORTLINK_API_KEY = os.environ.get("SHORTLINK_API_KEY", "635ac69ec616f795c158e4f51d2a2f3650dca14b")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', "86400"))
U_S_E_P = True if (True if os.environ.get('U_S_E_P', "False") == "TRUE" else False) and USE_SHORTLINK else False
TUT_VID = os.environ.get("TUT_VID", "https://t.me/unfiltered_stuf")

# Payment Settings
USE_PAYMENT = True if (True if os.environ.get("USE_PAYMENT", "TRUE") == "TRUE" else False) and USE_SHORTLINK else False
UPI_ID = os.environ.get("UPI_ID", "nitinkamboj510@fam")
UPI_IMAGE_URL = os.environ.get("UPI_IMAGE_URL", "@nitin_510")
SCREENSHOT_URL = os.environ.get("SCREENSHOT_URL", f"t.me/{OWNER_TAG}")

PRICE1 = os.environ.get("PRICE1", "40")
PRICE2 = os.environ.get("PRICE2", "70")
PRICE3 = os.environ.get("PRICE3", "210")
PRICE4 = os.environ.get("PRICE4", "420")
PRICE5 = os.environ.get("PRICE5", "ask owner")

# Force Join Message
FORCE_MSG = os.environ.get("FORCE_MSG", "𝚂𝚘𝚛𝚛𝚢 𝙳𝚞𝚍𝚎 𝚈𝚘𝚞 𝙽𝚎𝚎𝚍 𝚃𝚘 𝙹𝚘𝚒𝚗 𝚃𝚑𝚎𝚜𝚎 𝙲𝚑𝚊𝚗𝚗𝚎𝚕𝚜</b>\n\n<b>𝚂𝚘 𝙿𝚕𝚎𝚊𝚜𝚎 𝙲𝚕𝚒𝚌𝚔 𝙱𝚕𝚘𝚠 𝚃𝚘 𝙹𝚘𝚒𝚗 𝙲𝚑𝚊𝚗𝚗𝚎𝚕 🔥</b>")

CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>None</b>")

# Protection Settings
PROTECT_CONTENT = True if os.environ.get("PROTECT_CONTENT", "TRUE") == "TRUE" else False
DISABLE_CHANNEL_BUTTON = True if os.environ.get("DISABLE_CHANNEL_BUTTON", "TRUE") == "TRUE" else False

# Admin list
try:
    ADMINS = [int(x) for x in os.environ.get("ADMINS", "6667276878").split()]
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

ADMINS.append(OWNER_ID)

# Logging Settings
LOG_FILE_NAME = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
