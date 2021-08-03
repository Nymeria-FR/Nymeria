from typing import Text
from nymeria.message.info.fortnite import fortnite_stat


async def info_analyse(message):
    if message.content.startswith("n!pp"):
        if len(message.mentions) == 0:
            pp = message.author.avatar_url
            await message.channel.send(pp)
        else:
            for mention in message.mentions:
                pp = mention.avatar_url
                await message.channel.send(pp)
        return True
    elif message.content.startswith("n!fortnite"):
        await fortnite_stat(message)
    return False
