import discord
import config


class MyClient(discord.Client):
    async def on_ready(self):
        print("Start bot!")


client = MyClient()
client.run(str(config.token))