from random import randint


class Russe():

    def __init__(self, message):
        self.channel = message.channel

    async def launch(self):
        n = randint(1, 6)
        print(n)
        if n == 6:
            await self.channel.send("Pan ! Tu es mort")

        else:
            await self.channel.send("Bravo, tu as survécu")
