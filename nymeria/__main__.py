from discord import Intents
from nymeria import Bot
from dotenv import load_dotenv
import os

def main(token):
    Bot_intents = Intents.none()
    Bot_intents.members = True
    Bot_intents.invites = True
    Bot_intents.guilds = True
    Bot_intents.emojis = True
    Bot_intents.messages = True
    Bot_intents.guild_messages = True
    Bot_intents.dm_messages = True
    Bot_intents.reactions = True
    Bot_intents.guild_reactions = True
    Bot_intents.dm_reactions = True
    Totten = Bot(Bot_intents)
    Totten.run(token)

load_dotenv()
main(os.getenv("TOKEN"))