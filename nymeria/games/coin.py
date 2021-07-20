from discord import File
from random import randint


class Coin:
    """
	"""

    def __init__(self, message):
        self.channel = message.channel
        self.author = message.author

    async def launch(self):
        n = randint(0,1)
        if n == 0:
            await self.channel.send(f"{self.author.mention}\n Heads",file=File('donnees/totten.png'))
        else:
            await self.channel.send(f"{self.author.mention}\n Tails",file=File('donnees/totten2.png'))