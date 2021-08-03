from nymeria.message.fun.camion import camion
from nymeria.message.fun.other import love, compte

async def fun_analyse(message):
    if message.content.startswith("n!camion"):
        await camion(message)
        return True
    elif message.content.startswith("n!love"):
        await love(message)
        return True
    elif message.content.startswith("n!compte"):
        await compte(message)
        return True
    return False