from nymeria.message.moderation.delete import delete

from nymeria.message.moderation.ban import ban_analyse

from nymeria.message.moderation.mute import mute
from nymeria.message.moderation.mute import unmute

from nymeria.message.moderation.infos import infos


async def moderation_analyse(message):
    if message.content.startswith("n!del"):
        await delete(message)
        return True

    elif await ban_analyse(message):
        return True

    elif message.content.startswith("n!mute"):
        await mute(message)
        return True

    elif message.content.startswith("n!um"):
        await unmute(message)
        return True

    elif message.content.startswith("n!infos"):
        await infos(message)
        return True

    return False
