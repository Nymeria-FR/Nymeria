from nymeria import nymeria
from nymeria.message.moderation.analyse import moderation_analyse
from nymeria.message.games.game import game_analyse
from nymeria.message.info.info import info_analyse

@nymeria.event
async def on_message(message):
    if await moderation_analyse(message):
        return 

    elif await game_analyse(message):
        return

    elif await info_analyse(message):
        return

    '''

        

        if message.content.startswith("n!love"):
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

        if message.content.startswith("n!camion"):
            await message.delete()
            msg = message.content.split(" ")[1:]
            text = " ".join(msg)
            cam = await message.channel.send(
                f"""
──────────────────▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
───────────────▄▄██▌█ BEEP BEEP
────────────▄▄▄▌▐██▌█ {text}
────────────███████▌█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
────────────▀(@)▀▀▀▀▀▀▀(@)(@)▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
            )
            await ²sleep(1)
            await cam.edit(
                content=f"""
────────────────▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
─────────────▄▄██▌█ BEEP BEEP
──────────▄▄▄▌▐██▌█ {text}
──────────███████▌█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
──────────▀(@)▀▀▀▀▀▀▀(@)(@)▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
──────────────▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
───────────▄▄██▌█ BEEP BEEP
────────▄▄▄▌▐██▌█ {text}
────────███████▌█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
────────▀(@)▀▀▀▀▀▀▀(@)(@)▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
────────────▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
─────────▄▄██▌█ BEEP BEEP
──────▄▄▄▌▐██▌█ {text}
──────███████▌█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
──────▀(@)▀▀▀▀▀▀▀(@)(@)▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
──────────▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
───────▄▄██▌█ BEEP BEEP
────▄▄▄▌▐██▌█ {text}
────███████▌█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
────▀(@)▀▀▀▀▀▀▀(@)(@)▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
────────▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
─────▄▄██▌█ BEEP BEEP
──▄▄▄▌▐██▌█ {text}
──███████▌█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
──▀(@)▀▀▀▀▀▀▀(@)(@)▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
──────▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
───▄▄██▌█ BEEP BEEP
▄▄▄▌▐██▌█ {text}
███████▌█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
▀(@)▀▀▀▀▀▀▀(@)(@)▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
────▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
─▄▄██▌█ BEEP BEEP
▄▌▐██▌█ {text}
█████▌█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
@)▀▀▀▀▀▀▀(@)(@)▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
────▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
─▄▄██▌█ BEEP BEEP
▄▌▐██▌█ {text}
█████▌█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
@)▀▀▀▀▀▀▀(@)(@)▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
──▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
▄██▌█ BEEP BEEP
▐██▌█ {text}
███▌█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
▀▀▀▀▀▀▀(@)(@)▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
█▌█ BEEP BEEP
█▌█ {text}
█▌█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
▀▀▀▀▀(@)(@)▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
█ BEEP BEEP
█ {text}
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
▀▀▀(@)(@)▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
BEEP BEEP
{text}
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
▀(@)(@)▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
EP BEEP
{text}
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
@)(@)▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
 BEEP
{text}
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
(@)▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
▀▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
EEP
{text}
▄▄▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
)▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
P
{text}
▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌

{text}
▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌

{text}
▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
▀▀▀▀▀▀​▀▀▀▀▀▀▌

{text}
▄▄▄▄▄▄​▄▄▄▄▄▄▌
▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
▀▀▀▀​▀▀▀▀▀▀▌

{text}
▄▄▄▄​▄▄▄▄▄▄▌
▀▀▀▀​▀▀▀▀(@)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
▀▀​▀▀▀▀▀▀▌

{text}
▄▄​▄▄▄▄▄▄▌
▀▀​▀▀▀▀(@)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
​▀▀▀▀▀▀▌


​▄▄▄▄▄▄▌
​▀▀▀▀(@)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
​▀▀▀▀▌


​▄▄▄▄▌
​▀▀(@)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
​▀▀▌


​▄▄▌
​(@)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
​▌


​▌
​)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
​


​
​
            """
            )

        if message.content.startswith("n!compte"):
            k = 1
            nb = await message.channel.send(k)
            while True:
                k += 1
                await asyncio.sleep(1)
                await nb.edit(content=k)

'''