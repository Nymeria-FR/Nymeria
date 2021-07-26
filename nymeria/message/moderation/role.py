async def add_bot_role(member):
    if member.bot is True:
        guild = get_guild(861292008101642281)
        bot = guild.get_role(861292008101642286)
        await member.add_roles(bot)
        return True
    return False

async def add_member_role(self, member):
    for guild in self.guilds:
        if guild.id == 861292008101642281:
            for role in guild.roles:
                if role.id == 861292008101642287:
                    member_role = role
    await member.add_roles(member_role)