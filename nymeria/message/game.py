from discord import Message



class Game():
    """
    """
    def __init__(self, message, prefix):
        commande = message.content.split(' ')
        self.game = commande[1]
        self.message = message        

    async def launch(self, client):
        if(self.game == "bingo"):
            print("bingo")
        if(self.game == "capital"):
            print("capital")
        if(self.game == "pokemon"):
            print("pokemon")
        if(self.game == "rps"):
            print("rps")
        if(self.game == "coin"):
            print("coin")
        if(self.game == "pourcb"):
            print("pourcb")
        if(self.game == "pendu"):
            print("pendu")
        if(self.game == "scrabble"):
            print("scrabble")
        return   