import asyncio

import discord

client = discord.Client()


@client.event
async def on_ready():
    print('Wir sind eingeloggt als User {}'.format(client.user.name))
    client.loop.create_task(status_task())


async def status_task():
    while True:
        await client.change_presence(activity=discord.Game('discord.gg/devsky'), status=discord.Status.online)
        await asyncio.sleep(3)
        await client.change_presence(activity=discord.Game('Mein cooler Bot!'), status=discord.Status.online)
        await asyncio.sleep(3)


@client.event
async def on_message(message):
    if message.author.bot:
        return
    if '!help' in message.content:
        await message.channel.send('**Hilfe zum PyBot**\r\n'
                                   '!help - Zeigt diese Hilfe an')


client.run('')
