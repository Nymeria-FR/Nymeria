import asyncio
from random import randint


class Pendu:
    """
	"""

    def __init__(self, message):
        self.channel = message.channel
        self.author = message.author
        f = open("donnees/diko.txt","r")
        table = f.readlines()
        f.close()
        n = randint(1,len(table))
        self.mot = table[n].replace('\n', '')

    async def launch(self, client):
        print(self.mot)
        longueur = "**Devine :** " + '‿' * (int(len(self.mot)))
        reponse = '‿' * (int(len(self.mot))) 
        await self.channel.send(longueur)
        essais = 1
        trouve = []

        def is_correct(m):
            return len(m.content) == 1 and m.author == self.author
        def split(word): 
            return [char for char in word][0]
        def position(mot,lettre):
            pos = []
            for i in range(len(mot)):
                if mot[i] == lettre:
                    pos.append(i)
            return pos

        while (essais <= 6):
            guess = await client.wait_for(event="message",check=is_correct)
            lettre = split(guess.content).upper()
            print(trouve)

            if lettre in trouve:
                await self.channel.send(f"**{self.author.name}** Tu as déjà dit cette lettre")
            
            elif lettre in self.mot:
                trouve.append(lettre)
                tab = position(self.mot,lettre)
                caracteres = list(reponse)
                for i in range(len(tab)):
                    caracteres[tab[i]] = lettre
                reponse = "".join(caracteres)
                await self.channel.send(f"**Lettre donnée : **{lettre}\n**Devine :** {reponse}")
                if reponse.upper() == (self.mot).upper():
                    await self.channel.send(f"**{self.author.name}** Gagné ! Le mot était {self.mot}")
                    break

            else:
                trouve.append(lettre)
                if essais == 1:
                    await self.channel.send(f"""**Lettre donnée : **{lettre}
**{self.author.name}**, raté ! Nb d'erreurs : {essais}/6
```
  _______
 |/      |
 |      
 |      
 |       
 |      
 |
_|___
```
**Devine :** {reponse}
""")

                if essais == 2:
                    await self.channel.send(f"""**Lettre donnée : **{lettre}
**{self.author.name}**, raté ! Nb d'erreurs : {essais}/6
```
  _______
 |/      |
 |      (_)
 |      
 |       
 |      
 |
_|___
```
**Devine :** {reponse}
""")
                if essais == 3:
                    await self.channel.send(f"""**Lettre donnée : **{lettre}
**{self.author.name}**, raté ! Nb d'erreurs : {essais}/6
```
  _______
 |/      |
 |      (_)
 |       |
 |       |
 |      
 |
_|___
```
**Devine :** {reponse}
""")

                if essais == 4:
                    await self.channel.send(f"""**Lettre donnée : **{lettre}
**{self.author.name}**, raté ! Nb d'erreurs : {essais}/6
```
  _______
 |/      |
 |      (_)
 |      \|/
 |       |
 |      
 |
_|___
```
**Devine :** {reponse}
""")
                if essais == 5:
                    await self.channel.send(f"""**Lettre donnée : **{lettre}
**{self.author.name}**, raté ! Nb d'erreurs : {essais}/6
```
  _______
 |/      |
 |      (_)
 |      \|/
 |       |
 |      /
 |
_|___
```
**Devine :** {reponse}
""")

                if essais == 6:
                    perdu = await self.channel.send(f"""**Lettre donnée : **{lettre}
**{self.author.name}**, raté ! Nb d'erreurs : {essais}/6
```
  _______
 |/      |
 |      (x)
 |      \|/
 |       |
 |      / \\
 |
_|___
```
Perdu ! Le mot était {self.mot}
""")
                    
                
                    await asyncio.sleep(1)
                    await perdu.edit(content=f"""**Lettre donnée : **{lettre}
**{self.author.name}**, raté ! Nb d'erreurs : {essais}/6
```
  _______
 |/      |
 |      (x)
 |      _|_
 |       |
 |      / \\
 |
_|___
```
Perdu ! Le mot était {self.mot}
""")
                    await asyncio.sleep(1)
                    await perdu.edit(content=f"""**Lettre donnée : **{lettre}
**{self.author.name}**, raté ! Nb d'erreurs : {essais}/6
```
  _______
 |/      |
 |      (x)
 |       |
 |      /|\\
 |      / \\
 |
_|___
```
Perdu ! Le mot était {self.mot}
""")
                    break
                essais += 1