from nymeria.message.moderation.delete import delete

from nymeria.message.moderation.ban import ban
from nymeria.message.moderation.ban import unban
from nymeria.message.moderation.ban import kick
from nymeria.message.moderation.ban import banlist

from nymeria.message.moderation.mute import mute
from nymeria.message.moderation.mute import unmute

from nymeria.message.moderation.role import add_bot_role
from nymeria.message.moderation.role import add_member_role

from nymeria.message.moderation.banword import ban_word

from nymeria.message.moderation.infos import infos


async def moderation_analyse(message):
    if message.content.startswith("n!del"):
        await delete(message)
    
    elif message.content.startswith("n!banlist"):
        await banlist(message)

    elif message.content.startswith("n!ban"):
        await ban(message)

    elif message.content.startswith("n!ub"):
        await unban(message)

    elif message.content.startswith("n!kick"):
        await kick(message)

    elif message.content.startswith("n!mute"):
        await mute(message)

    elif message.content.startswith("n!um"):
        await unmute(message)

    elif message.content.startswith("n!infos"):
        await infos(message)

    return False