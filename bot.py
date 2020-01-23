import discord
import config


class MyClient(discord.Client):
    async def on_ready(self):
        print("{} вышел на связь!".format(self.user.name))

    async def on_message(self, message):
        async def add_reactIdeas():
            if (not config.channelIdeas or message.channel.id != config.channelIdeas):
                return
            for react in config.reactionsIdeas:
                await message.add_reaction(react)

        async def add_reactCreativity():
            if (not config.channelCreativity or message.channel.id != config.channelCreativity):
                return
            for react in config.reactionsCreativity:
                await message.add_reaction(react)

        await add_reactIdeas()
        await add_reactCreativity()


client = MyClient()
client.run(str(config.token))
