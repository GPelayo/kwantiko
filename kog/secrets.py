import copy
from typing import Dict


class SecretsManager:
    secrets = None  # type: Dict[str]

    def clone(self):
        return ClonedSecretsManager(self)


class ClonedSecretsManager(SecretsManager):
    def __init__(self, secrets_manager: SecretsManager):
        self.orignal_manager = secrets_manager
        self.secrets = copy.deepcopy(self.orignal_manager.secrets)
