import asyncio
import random

import discord
from discord import Member, Guild

client = discord.Client()

#########################################################################

antworten =['Ja', 'Nein', 'Vielleicht', 'Wahrscheinlich', 'Sieht so aus', 'Sehr wahrscheinlich',
            'Sehr unwahrscheinlich']


@client.event
async def on_ready():
    print('Wir sind eingeloggt als User {}'.format(client.user.name))
    client.loop.create_task(status_task())


async def status_task():
    colors = [discord.Colour.red(), discord.Colour.orange(), discord.Colour.gold(), discord.Colour.green(),
              discord.Colour.blue(), discord.Colour.purple()]
    while True:
        await client.change_presence(activity=discord.Game('discord.gg/devsky'), status=discord.Status.online)
        await asyncio.sleep(5)
        await client.change_presence(activity=discord.Game('Mein cooler Bot!'), status=discord.Status.online)
        await asyncio.sleep(5)
        if client.get_guild(658960248345853952):
            guild: Guild = client.get_guild(658960248345853952)
            role = guild.get_role(662606175862521856)
            if role:
                if role.position < guild.get_member(client.user.id).top_role.position:
                    await role.edit(colour=random.choice(colors))


def is_not_pinned(mess):
    return not mess.pinned


@client.event
async def on_message(message):
    if message.author.bot:
        return
    if '!help' in message.content:
        await message.channel.send('**Hilfe zum PyBot**\r\n'
                                   '!help - Zeigt diese Hilfe an')
    if message.content.startswith('!userinfo'):
        args = message.content.split(' ')
        if len(args) == 2:
            member: Member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
            if member:
                embed = discord.Embed(title='Userinfo für {}'.format(member.name),
                                      description='Dies ist eine Userinfo für den User {}'.format(member.mention),
                                      color=0x22a7f0)
                embed.add_field(name='Server beigetreten', value=member.joined_at.strftime('%d/%m/%Y, %H:%M:%S'),
                                inline=True)
                embed.add_field(name='Discord beigetreten', value=member.created_at.strftime('%d/%m/%Y, %H:%M:%S'),
                                inline=True)
                rollen = ''
                for role in member.roles:
                    if not role.is_default():
                        rollen += '{} \r\n'.format(role.mention)
                if rollen:
                    embed.add_field(name='Rollen', value=rollen, inline=True)
                embed.set_thumbnail(url=member.avatar_url)
                embed.set_footer(text='Ich bin ein EmbedFooter.')
                mess = await message.channel.send(embed=embed)
                await mess.add_reaction('🚍')
                await mess.add_reaction('a:tut_herz:662606955520458754')
    if message.content.startswith('!clear'):
        if message.author.permissions_in(message.channel).manage_messages:
            args = message.content.split(' ')
            if len(args) == 2:
                if args[1].isdigit():
                    count = int(args[1]) + 1
                    deleted = await message.channel.purge(limit=count, check=is_not_pinned)
                    await message.channel.send('{} Nachrichten gelöscht.'.format(len(deleted) - 1))
    if message.content.startswith('!8ball'):
        args = message.content.split(' ')
        if len(args) >= 2:
            frage = ' '.join(args[1:])
            mess = await message.channel.send('Ich versuche deine Frage `{0}` zu beantworten.'.format(frage))
            await asyncio.sleep(2)
            await mess.edit(content='Ich kontaktiere das Orakel...')
            await asyncio.sleep(2)
            await mess.edit(content='Deine Antwort zur Frage `{0}` lautet: `{1}`'
                            .format(frage, random.choice(antworten)))


client.run('')
