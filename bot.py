import discord
import config
from colors import out_green


class MyClient(discord.Client):
    async def on_ready(self):
        out_green("{} вышел на связь!".format(self.user.name))

    async def on_message(self, message):
        if (not config.channelIdeas or message.channel.id != config.channelIdeas):
            return
        for react in config.reactionsIdeas:
            await message.add_reaction(react)


client = MyClient()
client.run(str(config.token))
