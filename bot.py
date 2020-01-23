import discord
import config
from colors import out_green


class MyClient(discord.Client):
    async def on_ready(self):
        out_green("{} вышел на связь!".format(self.user.name))


client = MyClient()
client.run(str(config.token))
