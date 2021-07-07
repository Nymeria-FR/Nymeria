from discord import Message, Client, File
from random import randint
from time import time

class Bingo:
    """
	"""

    def __init__(self, message):
        commande = message.content.split(" ")
        self.number = int(commande[2]) if len(commande) >= 3 and commande[2].isdigit() else 10
        self.indic = True if len(commande) == 4 and commande[3] == "indic" else False
        self.inc = randint(1, self.number)
        self.channel = message.channel

    async def launch(self, client):
        def is_correct(m):
            return m.channel == self.channel and m.content.isdigit()

        await self.channel.send(
            f"Le bingo a commencé ! Trouvez le nombre entre 1 et {self.number}"
        )
        t1 = time()
        rep = -1
        print(self.inc)
        while rep != self.inc:
            guess = await client.wait_for(event="message", check=is_correct)
            rep = int(guess.content)
            if (rep) > self.inc and self.indic:
                #await self.channel.send("Your number is to big")
                await guess.add_reaction('⬇')
            if (rep) < self.inc and self.indic:
                #await self.channel.send("Your number is to small")
                await guess.add_reaction('⬆')
        t2 = time()
        await guess.add_reaction('✅')
        await self.channel.send(
            f"{guess.author.mention}\n🎉Bien joué, le nombre était {self.inc}🎉 (trouvé en {t2-t1:.1f} secondes)"
        )