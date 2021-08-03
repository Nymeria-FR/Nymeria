from nymeria import nymeria
from nymeria.message.moderation.analyse import moderation_analyse
from nymeria.message.games.game import game_analyse
from nymeria.message.info.info import info_analyse
from nymeria.message.fun.fun import fun_analyse

@nymeria.event
async def on_message(message):
    if await moderation_analyse(message):
        return 

    elif await game_analyse(message):
        return

    elif await info_analyse(message):
        return

    elif await fun_analyse(message):
        return
