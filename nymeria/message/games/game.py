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
        return True

    elif(game == "capital"):
        capital = Capital(message)
        await capital.launch(nymeria)
        return True

    elif(game == "pokemon"):
        pokemon = Pokemon(message)
        await pokemon.launch(nymeria)
        return True

    elif(game == "rps"):
        rps = RPS(message)
        await rps.launch(nymeria)
        return True

    elif(game == "coin"):
        coin = Coin(message)
        await coin.launch()
        return True

    elif(game == "pourcb"):
        pourcb = Pourcb(message)
        await pourcb.launch(nymeria)
        return True

    elif(game == "pendu"):
        pendu = Pendu(message)
        await pendu.launch(nymeria)
        return True

    elif(game == "scrabble"):
        scrabble = Scrabble(message)
        await scrabble.launch(nymeria)
        return True

    elif(game == "roulette"):
        russe = Russe(message)
        await russe.lauch(nymeria)
        
    return False
