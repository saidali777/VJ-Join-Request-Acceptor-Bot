from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

class Bot(Client):

    def __init__(self):
        super().__init__(
        "vj join request bot",
         api_id=API_ID,'12618934'
         api_hash=API_HASH,'49aacd0bc2f8924add29fb02e20c8a16'
         bot_token=BOT_TOKEN,'7934428209:AAF4VkZbSNnfK_JD1lHGXoEPu9zAo7kISB0'
         plugins=dict(root="plugins"),
         workers=50,
         sleep_threshold=10
        )

      
    async def start(self):
            
        await super().start()
        me = await self.get_me()
        self.username = '@' + me.username
            
        print('Bot Started Powered By @VJ_Botz')


    async def stop(self, *args):

        await super().stop()
        print('Bot Stopped Bye')

Bot().run()
