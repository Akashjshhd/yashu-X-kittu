from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "20536631"))
API_HASH = getenv("API_HASH", "b674f242e851d112a40870f9934f6d9c")
BOT_TOKEN = getenv("BOT_TOKEN", "5708694109:AAFsV7__TTzat9kyqeP2UouJVu77rzRRKAQ")
BOT_NAME = getenv("BOT_NAME", " YASHU X KITTU")
BOT_USERNAME = getenv("BOT_USERNAME", "GIRL_FRIEND_MUSIC_BOT")
OWNER_USERNAME = getenv("OWNER_USERNAME", "FRIEND_YASHU")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "Girl_Friend_group1m")
CHANNEL_UPDATES = getenv("CHANNEL_UPDATES", "fakechannel0i9")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "1000"))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "1000"))
START_IMG = getenv("START_IMG", "https://te.legra.ph/File-11-07-11")
PING_IMG = getenv("PING_IMG", "https://te.legra.ph/File-11-07-11")
SESSION_NAME = getenv("SESSION_NAME", "AQANVklZPfa4X_KQAb_B5jZKiEVP4W2TEyVu8ErRESidO0h_iEA_6PpZfugDX1L1hctHKyFpZt6J11yELJTmehk6yAuxdcOB5RHusDAs1btLulnHXAIrlCzDkJyUFXuWLlug0cg3iiYdL71uMJGrr67-6YZElCKnJmakCan9qCFcb0Vjb8mFlYeOwV7N4DTkmeYu_IlaE7ygk_b0Lhbnp8HiIIFZq_vgz1wK7HLv8U6hVGA_0eIvSHs6Te9wGQyr7sARzw7WDcvKftO6TB48iJC0aSO5aUiP5nZ25mFicBbJCGJlThH16SXD4DvijchRiRTzbXugceJVc75FSgEU-dryAAAAAUQaO7AA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5630731871").split()))
