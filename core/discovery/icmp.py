import subprocess 
import platform
import ipaddress
from . import DiscoveryEngine

class ICMPDiscovery(DiscoveryEngine):
    def discover(self, target_network: str) -> list[str]:
        # 1. Create the empty list BEFORE the loop starts
        active_hosts = []
        
        network = ipaddress.ip_network(target_network, strict=False)
        
        # 3. Start the loop
        for ip in network.hosts():
            # loops 256 times
            
            command = ["ping", "-c", "1", "-W", "100", str(ip)]

            # must run every single loop
            result = subprocess.run(
                command,
                capture_output=True,
                text=True
            )
            
            # 5. Check if the ping was successful (0 means success)
            if result.returncode == 0:
                print(f"[+] Active host found: {ip}")
                active_hosts.append(str(ip))
                
            # END

        # Return active hosts to main.py
        return active_hosts