from typing import Callable

from base import BaseSetting


class Scene(BaseSetting):
    create_npc_with_employer_id: Callable


scene = Scene()
