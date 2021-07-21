from nymeria.message.moderation.mod import deleteMessage

def analyse(message):
    if message.content.startswith("n!del"):
        print("del")

    if message.content.startswith("n!ban"):
        print("ban")

    if message.content.startswith("n!ub"):
        print("ub")

    if message.content.startswith("n!kick"):
        print("kick")

    if message.content.startswith("n!mute"):
        print("mute")

    if message.content.startswith("n!um"):
        print("um")
    
    if message.content.startswith("n!banlist"):
        print("banlist")
