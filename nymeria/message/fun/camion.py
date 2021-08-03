from asyncio import sleep
from nymeria import config


async def camion(message):
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
    await sleep(config.anonce_vitesse)
    await cam.edit(
        content=f"""
────────────────▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
─────────────▄▄██▌█ BEEP BEEP
──────────▄▄▄▌▐██▌█ {text}
──────────███████▌█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
──────────▀(@)▀▀▀▀▀▀▀(@)(@)▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
    )
    await sleep(config.anonce_vitesse)
    await cam.edit(
        content=f"""
──────────────▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
───────────▄▄██▌█ BEEP BEEP
────────▄▄▄▌▐██▌█ {text}
────────███████▌█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
────────▀(@)▀▀▀▀▀▀▀(@)(@)▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
    )
    await sleep(config.anonce_vitesse)
    await cam.edit(
        content=f"""
────────────▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
─────────▄▄██▌█ BEEP BEEP
──────▄▄▄▌▐██▌█ {text}
──────███████▌█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
──────▀(@)▀▀▀▀▀▀▀(@)(@)▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
    )
    await sleep(config.anonce_vitesse)
    await cam.edit(
        content=f"""
──────────▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
───────▄▄██▌█ BEEP BEEP
────▄▄▄▌▐██▌█ {text}
────███████▌█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
────▀(@)▀▀▀▀▀▀▀(@)(@)▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
    )
    await sleep(config.anonce_vitesse)
    await cam.edit(
        content=f"""
────────▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
─────▄▄██▌█ BEEP BEEP
──▄▄▄▌▐██▌█ {text}
──███████▌█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
──▀(@)▀▀▀▀▀▀▀(@)(@)▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
    )
    await sleep(config.anonce_vitesse)
    await cam.edit(
        content=f"""
──────▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
───▄▄██▌█ BEEP BEEP
▄▄▄▌▐██▌█ {text}
███████▌█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
▀(@)▀▀▀▀▀▀▀(@)(@)▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
    )
    await sleep(config.anonce_vitesse)
    await cam.edit(
        content=f"""
────▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
─▄▄██▌█ BEEP BEEP
▄▌▐██▌█ {text}
█████▌█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
@)▀▀▀▀▀▀▀(@)(@)▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
    )
    await sleep(config.anonce_vitesse)
    await cam.edit(
        content=f"""
────▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
─▄▄██▌█ BEEP BEEP
▄▌▐██▌█ {text}
█████▌█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
@)▀▀▀▀▀▀▀(@)(@)▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
    )
    await sleep(config.anonce_vitesse)
    await cam.edit(
        content=f"""
──▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
▄██▌█ BEEP BEEP
▐██▌█ {text}
███▌█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
▀▀▀▀▀▀▀(@)(@)▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
    )
    await sleep(config.anonce_vitesse)
    await cam.edit(
        content=f"""
▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
█▌█ BEEP BEEP
█▌█ {text}
█▌█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
▀▀▀▀▀(@)(@)▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
    )
    await sleep(config.anonce_vitesse)
    await cam.edit(
        content=f"""
▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
█ BEEP BEEP
█ {text}
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
▀▀▀(@)(@)▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
    )
    await sleep(config.anonce_vitesse)
    await cam.edit(
        content=f"""
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
BEEP BEEP
{text}
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
▀(@)(@)▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
    )
    await sleep(config.anonce_vitesse)
    await cam.edit(
        content=f"""
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
EP BEEP
{text}
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
@)(@)▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
    )
    await sleep(config.anonce_vitesse)
    await cam.edit(
        content=f"""
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
 BEEP
{text}
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
(@)▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
    )
    await sleep(config.anonce_vitesse)
    await cam.edit(
        content=f"""
▀▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
EEP
{text}
▄▄▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
)▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
    )
    await sleep(config.anonce_vitesse)
    await cam.edit(
        content=f"""
▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
P
{text}
▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
    )
    await sleep(config.anonce_vitesse)
    await cam.edit(
        content=f"""
▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌

{text}
▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
    )
    await sleep(config.anonce_vitesse)
    await cam.edit(
        content=f"""
▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌

{text}
▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
    )
    await sleep(config.anonce_vitesse)
    await cam.edit(
        content=f"""
▀▀▀▀▀▀​▀▀▀▀▀▀▌

{text}
▄▄▄▄▄▄​▄▄▄▄▄▄▌
▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
    )
    await sleep(config.anonce_vitesse)
    await cam.edit(
        content=f"""
▀▀▀▀​▀▀▀▀▀▀▌

{text}
▄▄▄▄​▄▄▄▄▄▄▌
▀▀▀▀​▀▀▀▀(@)▀
            """
    )
    await sleep(config.anonce_vitesse)
    await cam.edit(
        content=f"""
▀▀​▀▀▀▀▀▀▌

{text}
▄▄​▄▄▄▄▄▄▌
▀▀​▀▀▀▀(@)▀
            """
    )
    await sleep(config.anonce_vitesse)
    await cam.edit(
        content=f"""
​▀▀▀▀▀▀▌


​▄▄▄▄▄▄▌
​▀▀▀▀(@)▀
            """
    )
    await sleep(config.anonce_vitesse)
    await cam.edit(
        content=f"""
​▀▀▀▀▌


​▄▄▄▄▌
​▀▀(@)▀
            """
    )
    await sleep(config.anonce_vitesse)
    await cam.edit(
        content=f"""
​▀▀▌


​▄▄▌
​(@)▀
            """
    )
    await sleep(config.anonce_vitesse)
    await cam.edit(
        content=f"""
​▌


​▌
​)▀
            """
    )
    await sleep(config.anonce_vitesse)
    await cam.edit(
        content=f"""
​


​
​
            """
    )
