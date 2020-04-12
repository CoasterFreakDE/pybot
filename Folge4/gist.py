import random
from discord import Member, Guild

antworten =['Ja', 'Nein', 'Vielleicht', 'Wahrscheinlich', 'Sieht so aus', 'Sehr wahrscheinlich',
            'Sehr unwahrscheinlich']

colors = [discord.Colour.red(), discord.Colour.orange(), discord.Colour.gold(), discord.Colour.green(),
              discord.Colour.blue(), discord.Colour.purple()]
if client.get_guild(658960248345853952):
    guild: Guild = client.get_guild(658960248345853952)
    role = guild.get_role(662606175862521856)
    if role:
        if role.position < guild.get_member(client.user.id).top_role.position:
            await role.edit(colour=random.choice(colors))


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