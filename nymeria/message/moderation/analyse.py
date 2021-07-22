from nymeria.message.moderation.delete import delete


async def moderation_analyse(message):
    if message.content.startswith("n!del"):
        await delete(message)
        return True

    elif message.content.startswith("n!ban"):
        print("ban")
        return True

    elif message.content.startswith("n!ub"):
        print("ub")
        return True

    elif message.content.startswith("n!kick"):
        print("kick")
        return True

    elif message.content.startswith("n!mute"):
        print("mute")
        return True

    elif message.content.startswith("n!um"):
        print("um")
        return True

    elif message.content.startswith("n!banlist"):
        print("banlist")
        return True

    return False