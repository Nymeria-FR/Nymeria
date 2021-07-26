from discord import Embed

async def ban_word(message):
    await message.delete()
    embedVar = Embed(
        title="__**Warning**__ ⚠",
        url="http://www.nymeria.org/",
        description=f"{message.author.mention} \nAttention, tu as utilisé un mot interdit",
        color=0xF7AF00
    )
    embedVar.set_thumbnail(url=f"{message.author.avatar_url}")
    await message.channel.send(embed=embedVar)