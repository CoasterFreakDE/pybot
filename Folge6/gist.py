from discord import User

    if message.content.startswith('!ban') and message.author.guild_permissions.ban_members:
        args = message.content.split(' ')
        if len(args) == 2:
            member: Member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
            if member:
                await member.ban()
                await message.channel.send(f'Member {member.name} gebannt.')
            else:
                await message.channel.send(f'Kein user mit dem Namen {args[1]} gefunden.')
    if message.content.startswith('!unban') and message.author.guild_permissions.ban_members:
        args = message.content.split(' ')
        if len(args) == 2:
            user: User = discord.utils.find(lambda m: args[1] in m.user.name, await message.guild.bans()).user
            if user:
                await message.guild.unban(user)
                await message.channel.send(f'User {user.name} entbannt.')
            else:
                await message.channel.send(f'Kein user mit dem Namen {args[1]} gefunden.')
    if message.content.startswith('!kick') and message.author.guild_permissions.kick_members:
        args = message.content.split(' ')
        if len(args) == 2:
            member: Member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
            if member:
                await member.kick()
                await message.channel.send(f'Member {member.name} gekickt.')
            else:
                await message.channel.send(f'Kein user mit dem Namen {args[1]} gefunden.')