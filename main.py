# main.py
from core.discovery.icmp import ICMPDiscovery

def main():
    print("--- Starting Network Vulnerability Scanner ---")
    
    # Instantiate our discovery worker
    scanner = ICMPDiscovery()
    
    # Give it a test target network
    target = "10.177.84.0/24"
    
    # Trigger the discovery phase
    active_hosts = scanner.discover(target)
    
    print(f"Scan complete. Found hosts: {active_hosts}")

if __name__ == "__main__":
    main()