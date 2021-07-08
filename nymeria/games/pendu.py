import discord
from discord import Message, Client, File
from random import randint
from time import time
import csv

class Pendu:
    """
	"""

    def __init__(self, message):
        self.channel = message.channel
        self.author = message.author
        f = open("donnees/dico.txt","r")
        table = f.readlines()
        f.close()
        n = randint(1,len(table))
        self.mot = table[n]

    async def launch(self, client):
        print(self.mot)
        longueur = "**Devine :** " + '‿ ' * int(len(self.mot))
        await self.channel.send(longueur)
        essais = 1

        def is_correct(m):
            return len(m.content) == 1
        def split(word): 
            return [char for char in word][0]

        while (essais < 7):
            guess = await client.wait_for(event="message",check=is_correct)
            lettre = split(guess.content).upper()
            if longueur == self.mot:
                await self.channel.send("Gagné !")
                break
            if lettre in self.mot:
                longueur = "gngng"
                await self.channel.send("**Lettre donnée : **" + lettre)
                await self.channel.send(longueur)
            else:
                await self.channel.send("**Lettre donnée : **" + lettre)
                await self.channel.send(f"**{self.author.name}**, raté ! Nb d'erreurs : {essais}/6")

                if essais == 1:
                    await self.channel.send("""```
  _______
 |/      |
 |      
 |      
 |       
 |      
 |
_|___
```
""")

                if essais == 2:
                    await self.channel.send("""```
  _______
 |/      |
 |      (_)
 |      
 |       
 |      
 |
_|___
```
""")
                if essais == 3:
                    await self.channel.send("""```
  _______
 |/      |
 |      (_)
 |       |
 |       |
 |      
 |
_|___
```
""")

                if essais == 4:
                    await self.channel.send("""```
  _______
 |/      |
 |      (_)
 |      \|/
 |       |
 |      
 |
_|___
```
""")
                if essais == 5:
                    await self.channel.send("""```
  _______
 |/      |
 |      (_)
 |      \|/
 |       |
 |      //
 |
_|___
```
""")

                if essais == 6:
                    await self.channel.send("""```
  _______
 |/      |
 |      (x)
 |      \|/
 |       |
 |      //
 |
_|___
```
""")


                essais += 1
        
        await self.channel.send("Perdu !")
