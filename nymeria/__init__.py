from nymeria.config import TomlConfig

global config
config = TomlConfig("../config.toml", "../config.template.toml")

from discord import Client, Intents

default_intents = Intents.default()
default_intents.members = True
default_intents.voice_states = True
default_intents.invites = True

nymeria = Client(intents=default_intents)