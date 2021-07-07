from discord import Message, Client, File, DMChannel
from random import randint
from time import time


class Pourcb:
    """
	"""

    def __init__(self, message):
        self.author = message.author
        self.content = message.content
        self.channel = message.channel
        self.mention1 = message.mentions[0]
        commande = message.content.split(" ")
        self.number = int(commande[2]) if len(commande) >= 3 and commande[2].isdigit() else 10
        #self.mention2 = message.mentions[1]


    async def launch(self, client):

        await self.mention1.send(f"Donne un nombre entre 1 et {self.number}")  
        await self.author.send(f"Donne un nombre entre 1 et {self.number}") #mention2->author
			
        def is_correct1(m):
            return m.author == self.mention1 and m.content.isdigit() and isinstance(m.channel, DMChannel)
        def is_correct2(m):
            return m.author == self.author and m.content.isdigit() and isinstance(m.channel, DMChannel) #mention2->author
			
        guess1 = await client.wait_for('message', check=is_correct1)
        guess2 = await client.wait_for('message', check=is_correct2)
        rep1 = int(guess1.content)
        rep2 = int(guess2.content)
        print(rep1,rep2)
        if rep1 == rep2:
            await self.channel.send(f'{self.mention1.mention} {self.author.mention}\nGagné, vous avez tous les deux choisi {rep1}')
        else :
            await self.channel.send(f'Perdu, {self.mention1.mention} a choisi {rep1} et {self.author.mention} a choisi {rep2}')