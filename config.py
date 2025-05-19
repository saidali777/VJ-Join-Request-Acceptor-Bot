from os import environ

API_ID = int(environ.get("API_ID", "12618934"))
API_HASH = environ.get("API_HASH", "49aacd0bc2f8924add29fb02e20c8a16")
BOT_TOKEN = environ.get("BOT_TOKEN", "7934428209:AAF4VkZbSNnfK_JD1lHGXoEPu9zAo7kISB0")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002608373784"))
ADMINS = int(environ.get("ADMINS", "7837304801"))
DB_URI = environ.get("DB_URI", "mongodb+srv://madarazbotz:aemHxtb49hACpjd6@cluster0.ed7e2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = environ.get("DB_NAME", "Cluster0")
