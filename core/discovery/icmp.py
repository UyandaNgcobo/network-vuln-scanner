import subprocess 
import platform
import ipaddress
import concurrent.futures  # New library for multi-threading
from . import DiscoveryEngine

class ICMPDiscovery(DiscoveryEngine):
    
    # internal_method
    def _ping_host(self, ip) -> str:
        command = ["ping", "-c", "1", "-W", "100", str(ip)]
        result = subprocess.run(command, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"[+] Active host found: {ip}")
            return str(ip)
        return None

    # The Main Method
    def discover(self, target_network: str) -> list[str]:
        active_hosts = []
        network = ipaddress.ip_network(target_network, strict=False)
        
        print(f"[*] Starting concurrent scan on {target_network}...")
        
        # Thread pool
        with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
            
            # executor.map automatically loops through network.hosts() 
            # and passes each IP to _ping_host helper method
            results = executor.map(self._ping_host, network.hosts())
            
            # Collect the results as they finish
            for result in results:
                if result is not None:
                    active_hosts.append(result)
                    
        return active_hosts