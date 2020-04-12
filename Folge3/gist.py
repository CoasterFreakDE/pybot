def is_not_pinned(mess):
    return not mess.pinned

if message.content.startswith('!clear'):
    if message.author.permissions_in(message.channel).manage_messages:
        args = message.content.split(' ')
        if len(args) == 2:
            if args[1].isdigit():
                count = int(args[1])+1
                deleted = await message.channel.purge(limit=count, check=is_not_pinned)
                await message.channel.send('{} Nachrichten gelöscht.'.format(len(deleted)-1))