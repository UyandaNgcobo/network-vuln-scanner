import subprocess #run invisible terminal and write commands
import platform
import ipaddress
from . import DiscoveryEngine

class ICMPDiscovery(DiscoveryEngine):
    def discover(self, target_network: str) -> list[str]:
        network = ipaddress.ip_network(target_network, strict=False)
        for ip in network.hosts():
            print(f"I am getting ready to ping: {ip}")
            command = ["ping", "-c", "1", "-W", "100", str(ip)]

        result = subprocess.run(
            command,
            capture_output=True,
            text=True
        )
        

        print("--- THE TERMINAL OUTPUT ---")
        print(result.stdout)
        print("--- THE EXIT CODE ---")
        print(result.returncode)
        pass