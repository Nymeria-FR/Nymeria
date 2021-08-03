from random import randint
from asyncio import sleep


async def love(message):
    if len(message.content.split(" ")) < 2:
        await message.channel.send(
            f"{message.author.mention}\nTu ne m'as donné personne en paramètre"
        )
        return
    mention = message.mentions[0].mention
    love = randint(0, 100)
    await message.channel.send(
        f"__{love}%__ d'amour entre {message.author.mention} et {mention} ❤"
    )


async def compte(message):
    commande = message.content.split(" ")
    if len(commande) < 2:
        await message.channel.send(
            f"{message.author.mention}\nTu ne m'as pas donné de chiffres en paramètre"
        )
        return
    if not commande[1].isdigit():
        await message.channel.send(
            f"{message.author.mention}\n{commande[1]} n'est pas un chiffre"
        )
        return
    max = int(commande[1])
    nb = await message.channel.send(0)
    for k in range(1, max + 1):
        await sleep(1)
        await nb.edit(content=k)
