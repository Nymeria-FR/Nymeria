from nymeria import nymeria, config

from nymeria.join import on_member_join, on_member_remove
from nymeria.ready import on_ready


nymeria.run(config.token)
