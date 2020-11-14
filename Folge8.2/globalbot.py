import json
import os
from datetime import datetime

import discord
import pytz
from discord import Message, Guild, TextChannel, Permissions
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

if os.path.isfile("servers.json"):
    with open('servers.json', encoding='utf-8') as f:
        servers = json.load(f)
else:
    servers = {"servers": []}
    with open('servers.json', 'w') as f:
        json.dump(servers, f, indent=4)


@bot.command()
async def addGlobal(ctx):
    if ctx.author.guild_permissions.administrator:
        if not guild_exists(ctx.guild.id):
            server = {
                "guildid": ctx.guild.id,
                "channelid": ctx.channel.id,
                "invite": f'{(await ctx.channel.create_invite()).url}'
            }
            servers["servers"].append(server)
            with open('servers.json', 'w') as f:
                json.dump(servers, f, indent=4)
            embed = discord.Embed(title="**Willkommen im GlobalChat von Melion.net™**",
                                  description="Dein Server ist einsatzbereit!"
                                              " Ab jetzt werden alle Nachrichten in diesem Channel direkt an alle"
                                              " anderen Server weitergeleitet!",
                                  color=0x2ecc71)
            embed.set_footer(text='Bitte beachte, dass im GlobalChat stets ein Slowmode von mindestens 5 Sekunden'
                                  ' gesetzt sein sollte.')
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(description="Du hast bereits einen GlobalChat auf deinem Server.\r\n"
                                              "Bitte beachte, dass jeder Server nur einen GlobalChat besitzen kann.",
                                  color=0x2ecc71)
            await ctx.send(embed=embed)


@bot.command()
async def removeGlobal(ctx):
    if ctx.member.guild_permissions.administrator:
        if guild_exists(ctx.guild.id):
            globalid = get_globalChat_id(ctx.guild.id)
            if globalid != -1:
                servers["servers"].pop(globalid)
                with open('servers.json', 'w') as f:
                    json.dump(servers, f, indent=4)
            embed = discord.Embed(title="**Auf Wiedersehen!**",
                                  description="Der GlobalChat wurde entfernt. Du kannst ihn jederzeit mit"
                                              " `!addGlobal` neu hinzufügen",
                                  color=0x2ecc71)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(description="Du hast noch keinen GlobalChat auf deinem Server.\r\n"
                                              "Füge einen mit `!addGlobal` in einem frischen Channel hinzu.",
                                  color=0x2ecc71)
            await ctx.send(embed=embed)


#########################################

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if not message.content.startswith('!'):
        if get_globalChat(message.guild.id, message.channel.id):
            await sendAll(message)
    await bot.process_commands(message)


#########################################

async def sendAll(message: Message):
    conent = message.content
    author = message.author
    attachments = message.attachments
    de = pytz.timezone('Europe/Berlin')
    embed = discord.Embed(description=conent, timestamp=datetime.now().astimezone(tz=de), color=author.color)

    icon = author.avatar_url
    embed.set_author(name=author.name, icon_url=icon)

    icon_url = "https://i.giphy.com/media/xT1XGzYCdltvOd9r4k/source.gif"
    icon = message.guild.icon_url
    if icon:
        icon_url = icon
    embed.set_thumbnail(url=icon_url)
    embed.set_footer(text=f'Gesendet von Server {message.guild.name}', icon_url=icon_url)

    links = '[Melion Discord](https://discord.gg/j6nAhV6) ║ '
    globalchat = get_globalChat(message.guild.id, message.channel.id)
    if len(globalchat["invite"]) > 0:
        invite = globalchat["invite"]
        if 'discord.gg' not in invite:
            invite = 'https://discord.gg/{}'.format(invite)
        links += f'[Server Invite]({invite})'

    embed.add_field(name='⠀', value='⠀', inline=False)
    embed.add_field(name='Links & Hilfe', value=links, inline=False)

    if len(attachments) > 0:
        img = attachments[0]
        embed.set_image(url=img.url)

    for server in servers["servers"]:
        guild: Guild = bot.get_guild(int(server["guildid"]))
        if guild:
            channel: TextChannel = guild.get_channel(int(server["channelid"]))
            if channel:
                perms: Permissions = channel.permissions_for(guild.get_member(bot.user.id))
                if perms.send_messages:
                    if perms.embed_links and perms.attach_files and perms.external_emojis:
                        await channel.send(embed=embed)
                    else:
                        await channel.send('{0}: {1}'.format(author.name, conent))
                        await channel.send('Es fehlen einige Berechtigungen. '
                                           '`Nachrichten senden` `Links einbetten` `Datein anhängen`'
                                           '`Externe Emojis verwenden`')
    await message.delete()


###############################

def guild_exists(guildid):
    for server in servers['servers']:
        if int(server['guildid'] == int(guildid)):
            return True
    return False


def get_globalChat(guild_id, channelid=None):
    globalChat = None
    for server in servers["servers"]:
        if int(server["guildid"]) == int(guild_id):
            if channelid:
                if int(server["channelid"]) == int(channelid):
                    globalChat = server
            else:
                globalChat = server
    return globalChat


def get_globalChat_id(guild_id):
    globalChat = -1
    i = 0
    for server in servers["servers"]:
        if int(server["guildid"]) == int(guild_id):
            globalChat = i
        i += 1
    return globalChat


###########################################################

bot.run('NjU4OTU5MTU2ODk1ODA5NTU3.XtTulA.dlyP6WQFBTIFSkP9QLdZZ7PGPlY')
