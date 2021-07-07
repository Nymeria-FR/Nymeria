from discord import Message, Client, File
from random import randint
from time import time
import csv

class Pokemon:
    """
	"""

    def __init__(self, message):
        self.channel = message.channel
        self.author = message.author
        f = open("donnees/pokemonTri.csv","r")
        table = list(csv.reader(f, delimiter=','))
        f.close()
        n = randint(1,len(table))
        self.name = table[n]
        self.pokemon = self.name[0] + '.png'
        self.name = self.name[0]
        self.chemin = "donnees/images/" + self.pokemon

    async def launch(self, client):
        
        def is_correct(m):
            return m.channel == self.channel and m.author == self.author

        await self.channel.send(f"Quel est ce Pokémon ? ")
        t1 = time()
        await self.channel.send(file=File(self.chemin))
        print(self.name)
        message = await client.wait_for(event="message", check=is_correct)
        t2 = time()
        guess = message.content.lower()
        if guess == self.name:
            await self.channel.send(
                f"{message.author.mention}\n🎉Bien joué, le Pokémon était {self.name}🎉 (trouvé en {t2-t1:.1f} secondes)"
            )
        else:
            await self.channel.send(
                f"{message.author.mention}\nDésolé, le Pokémon était {self.name}"
            )