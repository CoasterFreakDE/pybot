from discord import Guild

autoroles = {
    658960248345853952: {'memberroles': [667129769397059596, 667129722995474460], 'botroles': [667129686131736586]},
    643782995869827092: {'memberroles': [], 'botroles': []}
}



    guild: Guild = member.guild


        autoguild = autoroles.get(member.guild.id)
        if autoguild and autoguild['memberroles']:
            for roleId in autoguild['memberroles']:
                role = guild.get_role(roleId)
                if role:
                    await member.add_roles(role, reason='AutoRoles', atomic=True)
    else:
        autoguild = autoroles.get(member.guild.id)
        if autoguild and autoguild['botroles']:
            for roleId in autoguild['botroles']:
                role = guild.get_role(roleId)
                if role:
                    await member.add_roles(role, reason='AutoRoles', atomic=True)