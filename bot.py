import discord
import config
import collections
import random
import tracemalloc
import asyncio

tracemalloc.start()

numberNaN = collections.Counter()

def isNaN(string):
    return not string.isdigit()
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

        async def counting():
            if (message.channel.id != config.channelCounting):
                return
            messages = await message.channel.history(limit=2).flatten()
            oldText = messages[1].content.split(" ")[0]
            newText = message.content.split(" ")[0]
            a = int(oldText) + 1
            text = message.content.split(" ")[0]
            if (numberNaN[messages[1].author.id]):
                await message.author.send(content="Да падажди ты, видышь ведь что участник не дописал число. Вот снимется с него крестик и пиши потом.")
                await message.delete()
                return

            async def messageDelete():
                react = config.errorReact[random.randint(
                    0, len(config.errorReact) - 1)]
                await message.add_reaction(react)
                numberNaN[message.author.id] = {"id": message.id}
                async def code():
                    message2 = await self.get_channel(message.channel.id).fetch_message(message.id)
                    newText2 = message2.content.split(" ")[0]
                    if (text == newText2 or isNaN(newText2) or a != int(newText2)):
                        await message2.delete()
                        del numberNaN[message2.author.id]
                    else:
                        del numberNaN[message2.author.id]
                        await message.remove_reaction(react, self.user)
                await asyncio.sleep(7)
                await code()
            if (isNaN(oldText)):
                await messages[1].delete()
                del numberNaN[messages[1].author.id]
                await message.delete()
            elif(messages[1].author.id == message.author.id):
                await message.delete()
            elif(isNaN(newText) or str(a) != newText):
                await messageDelete()
            else:
                del numberNaN[message.author.id]
        await add_reactIdeas()
        await add_reactCreativity()
        await counting()

    async def on_message_edit(self, before, after):
        if (after.channel.id != config.channelCounting or (numberNaN[after.author.id] and numberNaN[after.author.id]['id'] == after.id)):
            return
        newText = after.content.split(" ")[0]
        oldText = before.content.split(" ")[0]
        if (not newText.isdigit() or oldText != newText):
            await after.delete()
            return


client = MyClient()
client.run(str(config.token))
