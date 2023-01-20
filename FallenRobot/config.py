class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = "22617384"
    API_HASH = "1e73a59e5b4efa2c79ba97d0ebaff5ba"

    CASH_API_KEY = "SADHAZ7VT717K66N"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://khqyugaw:cCzP6_5GB_99XUEWfnK2SkR91M1fcqo6@berry.db.elephantsql.com/khqyugaw"  # A sql database url from elephantsql.com

    EVENT_LOGS = ()  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://Botmusic:Md6L7xvSBTo6dkmt@cluster0.wlwhub6.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/40eb1ed850cdea274693e.jpg"

    SUPPORT_CHAT = "idoganzzbot"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "5959599432:AAEt2EjvE8FfTY4M9z-QovEiyCpcdMw79Eo"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "WJLELU3365VQ"  # Get this value from https://timezonedb.com/api

    OWNER_ID = "5883111731"  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = "5916334430"  # List of groups that you want blacklisted.
    DRAGONS = "5916334430"  # User id of sudo users
    DEV_USERS = "5916334430"  # User id of dev users
    DEMONS = "5916334430"  # User id of support users
    TIGERS = "5916334430"  # User id of tiger users
    WOLVES = "5916334430"  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True

