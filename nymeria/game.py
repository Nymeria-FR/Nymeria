from discord import Message

from games.bingo import Bingo
from games.capital import Capital
from games.pokemon import Pokemon
from games.rps import RPS
from games.coin import Coin
from games.pourcb import Pourcb
from games.pendu import Pendu
from games.scrabble import Scrabble


class Game():
    """
    """
    def __init__(self, message, prefix):
        commande = message.content.split(' ')
        self.game = commande[1]
        self.message = message        

    async def launch(self, client):
        if(self.game == "bingo"):
            bingo = Bingo(self.message)
            await bingo.launch(client)
        if(self.game == "capital"):
            capital = Capital(self.message)
            await capital.launch(client)
        if(self.game == "pokemon"):
            pokemon = Pokemon(self.message)
            await pokemon.launch(client)
        if(self.game == "rps"):
            rps = RPS(self.message)
            await rps.launch(client)
        if(self.game == "coin"):
            coin = Coin(self.message)
            await coin.launch(client)
        if(self.game == "pourcb"):
            pourcb = Pourcb(self.message)
            await pourcb.launch(client)
        if(self.game == "pendu"):
            pendu = Pendu(self.message)
            await pendu.launch(client)
        if(self.game == "scrabble"):
            scrabble = Scrabble(self.message)
            await scrabble.launch(client)
        return   