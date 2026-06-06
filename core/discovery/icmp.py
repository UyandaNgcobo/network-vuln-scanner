import subprocess
import platform
from . import DiscoveryEngine

class ICMPDiscovery(DiscoveryEngine):
    def discover(self, target_network: str) -> list[str]:
        pass