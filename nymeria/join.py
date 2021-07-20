import datetime

from pytz import timezone
from discord import Embed

from . import config, nymeria
from .utility import get_guild

global invites
invites = dict()


async def get_invites():
    for data in config.servers.values():
        invites[data["id"]] = await nymeria.get_guild(data["id"]).invites()


async def update_guild(id):
    invites[id] = await nymeria.get_guild(id).invites()


async def get_inviter(member):
    new_invites = await member.guild.invites()
    for invite in range(len(new_invites)):
        if new_invites[invite].uses > invites[861292008101642281][invite].uses:
            print(new_invites[invite].uses, invites[861292008101642281][invite].uses)
            return new_invites[invite].inviter.name


async def add_bot_role(member, guild):
    if not member.bot:
        return False
    await member.add_roles(nymeria.get_guild(guild["id"]).get_role(guild["bot_role"]))
    return True


async def welcome_message(member, guild):
    inviter = await get_inviter(member)

    welcome_channel = nymeria.get_channel(guild["welcome_channel"])
    rules_channel = nymeria.get_channel(guild["role_channel"])
    date = datetime.datetime.now(timezone("Europe/Berlin"))
    invite_message = "・Tu as utilisé l'invitation de **{}**".format(inviter)

    if inviter == None:
        invite_message = "Tu as utilisé une invitation vanity"

    embedVar = Embed(
        title="Bienvenue !",
        url="http://www.nymeria.org/",
        description=guild["description"].format(
            member.mention, rules_channel.mention, inviter
        ) + invite_message,
        color=0xF7AF00,
        timestamp=date,
    )
    embedVar.set_thumbnail(url=f"{member.avatar_url}")
    await welcome_channel.send(embed=embedVar)


async def member_count(guild, member):
    newname = "Membres: {}".format(str(member.guild.member_count))
    await nymeria.get_channel(guild["member_count"]).edit(name=newname)


@nymeria.event
async def on_invite_create(invite):
    await update_guild(invite.guild.id)


@nymeria.event
async def on_invite_delete(invite):
    await update_guild(invite.guild.id)


@nymeria.event
async def on_member_join(member):
    guild = get_guild(member.guild.id)
    if guild != None:
        bot = await add_bot_role(member, guild)
        if bot is False:
            await welcome_message(member, guild)
            await update_guild(member.guild.id)
        await member_count(guild, member)


@nymeria.event
async def on_member_remove(member):
    guild = get_guild(member.guild.id)
    if guild != None:
        await member_count(guild, member)