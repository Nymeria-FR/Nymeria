from nymeria.message.games import *
from nymeria import nymeria

async def game_analyse(message):
    commande = message.content.split(" ")
    if len(commande) < 2:
        return False
    game = commande[1]

    if(game == "bingo"):
        bingo = Bingo(message)
        await bingo.launch(nymeria)

    elif(game == "capital"):
        capital = Capital(message)
        await capital.launch(nymeria)

    elif(game == "pokemon"):
        pokemon = Pokemon(message)
        await pokemon.launch(nymeria)

    elif(game == "rps"):
        rps = RPS(message)
        await rps.launch(nymeria)

    elif(game == "coin"):
        coin = Coin(message)
        await coin.launch()

    elif(game == "pourcb"):
        pourcb = Pourcb(message)
        await pourcb.launch(nymeria)

    elif(game == "pendu"):
        pendu = Pendu(message)
        await pendu.launch(nymeria)

    elif(game == "scrabble"):
        scrabble = Scrabble(message)
        await scrabble.launch(nymeria)

    return True
