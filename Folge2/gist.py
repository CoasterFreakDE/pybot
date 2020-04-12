#  imports
from discord import Member

#  on_message(message)
if message.content.startswith('!userinfo'):
	args = message.content.split(' ')
	if len(args) == 2:
		member: Member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
		if member:
			embed = discord.Embed(title='Userinfo für {}'.format(member.name),
								  description='Dies ist die Userinfo für den User {}'.format(member.mention),
								  color=0x22a7f0)
			embed.add_field(name='Server beigetreten', value=member.joined_at.strftime("%m/%d/%Y, %H:%M:%S"),
							inline=True)
			embed.add_field(name='Discord beigetreten', value=member.created_at.strftime("%m/%d/%Y, %H:%M:%S"),
							inline=True)
			rollen = ''
			for role in member.roles:
				if not role.is_default():
					rollen += '{} \r\n'.format(role.mention)
			if rollen:
				embed.add_field(name='Rollen', value=rollen, inline=True)
			embed.set_thumbnail(url=message.author.avatar_url)
			embed.set_footer(text='Ich bin ein EmbedFooter!')
			message = await message.channel.send(embed=embed)
			await message.add_reaction('🚍')
			await message.add_reaction('a:tut_herz:662606955520458754')