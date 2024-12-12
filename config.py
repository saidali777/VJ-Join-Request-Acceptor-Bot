from os import environ

API_ID = int(environ.get("API_ID", "28243586"))
API_HASH = environ.get("API_HASH", "4022d5686b9b7a7cf8891205921a0ab3")
BOT_TOKEN = environ.get("BOT_TOKEN", "7566645218:AAESBbzZYtnQDLb18QrSMdZR3-HxKWkrSUY")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002328437358"))
ADMINS = int(environ.get("ADMINS", ""))
DB_URI = environ.get("DB_URI", "mongodb+srv://madarazbotz:aemHxtb49hACpjd6@cluster0.ed7e2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = environ.get("DB_NAME", "Cluster0")
