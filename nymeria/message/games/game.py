from nymeria.message.games.bingo import Bingo
from nymeria import nymeria

async def launch(message, game):
    if(game == "bingo"):
        bingo = Bingo(message)
        await bingo.launch(nymeria)

    if(game == "capital"):
        print("capital")

    if(game == "pokemon"):
        print("pokemon")

    if(game == "rps"):
        print("rps")

    if(game == "coin"):
        print("coin")

    if(game == "pourcb"):
        print("pourcb")

    if(game == "pendu"):
        print("pendu")

    if(game == "scrabble"):
        print("scrabble")

    return

"""
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
        return
"""