from random import randint


class Russe(self,message):

    def __init__(self,message):
        self.channel = message.channel


    async def launch(self,client):

        n = randint(1,6)
        if n == 6: 
            await message.channel.send("Pan ! Tu es mort")

        else : 
            await message.channel.send("Bravo, tu as survécu")