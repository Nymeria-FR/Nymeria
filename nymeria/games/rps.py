from discord import Message, Client, File
from random import randint
from time import time


class RPS:
    """
	"""

    def __init__(self, message):
        self.channel = message.channel
        self.author = message.author
        # tab = ['Rock','Paper','Scissors']
        self.tab = ["🪨", "📰", "✂"]

    async def launch(self, client):
        botplay = self.tab[randint(0, 2)]

        def check(reaction, user):
            return user == self.author and (
                str(reaction.emoji) == "🪨"
                or str(reaction.emoji) == "📰"
                or str(reaction.emoji) == "✂"
            )

        while True:
            respons = await self.channel.send("Rock, Paper or Scissors")
            for emot in self.tab:
                await respons.add_reaction(emot)
            guess = await client.wait_for(event="reaction_add", check=check)
            guess = str(guess[0].emoji)
            if guess == botplay:
                await self.channel.send(
                    f"{self.author.mention}\nEquality, I have chosen {botplay}."
                )
                botplay = self.tab[randint(0, 2)]

            elif (
                (guess == "🪨" and botplay == "✂")
                or (guess == "📰" and botplay == "🪨")
                or (guess == "✂" and botplay == "📰")
            ):
                await self.channel.send(
                    f"{self.author.mention}\nGG, I have chosen {botplay} so you won "
                )
                break

            else:
                await self.channel.send(
                    f"{self.author.mention}\nSorry, I have chosen {botplay} so you lost "
                )
                break