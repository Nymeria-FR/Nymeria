async def delete(message):
    commande = message.content.split(" ")
    number = 100
    for word in commande:
        if word.isdigit():
            number = int(word)

    def check(message):
        return True

    if len(commande) == 1:
        await message.channel.purge()

    elif len(message.mentions) != 0:
        global mentions
        mentions = [message.mentions[0].id]
        for i in range(1, len(message.mentions)):
            mentions += message.mentions[i].id

        def check(message):
            return message.author.id in mentions

    await message.channel.purge(limit=number, check=check)
