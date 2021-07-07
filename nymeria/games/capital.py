from discord import Message, Client, File
from random import randint
import csv

class Capital:
    """
	"""

    def __init__(self, message):
        self.channel = message.channel
        self.author = message.author
        f = open("donnees/concap.csv","r")
        table = list(csv.reader(f, delimiter=','))
        f.close()
        n = randint(1,len(table))
        pays = table[n]
        self.nom = pays[0]
        self.capitale = pays[1].lower()

    async def launch(self, client):
        def is_correct(m):
            return m.channel == self.channel and m.author == self.author

        await self.channel.send(
            f"What is the capital of : {self.nom} ? "
        )
        print(self.capitale)
        message = await client.wait_for(event="message", check=is_correct)
        guess = message.content.lower()
        if guess == self.capitale:
            await self.channel.send(
                f"{message.author.mention}\n🎉Well done, the capital was {self.capitale}🎉"
            )
        else:
            await self.channel.send(
                f"{message.author.mention}\nSorry, the capital was {self.capitale}"
            )