@client.event
async def on_member_join(member):
    if not member.bot:
        embed = discord.Embed(title='Willkommen auf Melion {} <a:tut_herz:662606955520458754>'.format(member.name),
                              description='Wir heißen dich hier auf dem Server herzlich Willkommen',
                              color=0x22a7f0)
        try:
            if not member.dm_channel:
                await member.create_dm()
            await member.dm_channel.send(embed=embed);
        except discord.errors.Forbidden:
            print('Es konnte keine Willkommensnachricht an {0} gesendet werden.'.format(member.name))