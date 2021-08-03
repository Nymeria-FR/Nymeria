from . import config


def get_guild(id):
    for server, values in config.servers.items():
        if values["id"] == id:
            return config.servers[server]
