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
        longueur = "**Devine :** " + '‿' * (int(len(self.mot)) - 1)
        reponse = '‿' * (int(len(self.mot)) - 1) 
        await self.channel.send(longueur)
        essais = 1

        def is_correct(m):
            return len(m.content) == 1
        def split(word): 
            return [char for char in word][0]
        def position(mot,lettre):
            pos = []
            for i in range(len(mot)):
                if mot[i] == lettre:
                    pos.append(i)
            return pos

        while (essais < 7):
            guess = await client.wait_for(event="message",check=is_correct)
            lettre = split(guess.content).upper()
            
            if lettre in self.mot:
                tab = position(self.mot,lettre)
                caracteres = list(reponse)
                for i in range(len(tab)):
                    caracteres[tab[i]] = lettre
                reponse = "".join(caracteres)
                await self.channel.send("**Lettre donnée : **" + lettre)
                await self.channel.send("**Devine :** " + reponse)

                print(reponse.upper(),(self.mot).upper())

                if reponse.upper() == (self.mot).upper():
                    await self.channel.send("Gagné !")
                    break

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
        
        await self.channel.send(f"Perdu ! Le mot était {self.mot}")
