# main.py
from core.discovery.icmp import ICMPDiscovery

def main():
    print("--- Starting Network Vulnerability Scanner ---")
    
    # 1. Instantiate our discovery worker
    scanner = ICMPDiscovery()
    
    # 2. Give it a test target network
    target = "8.8.8.0/24"
    
    # 3. Trigger the discovery phase
    active_hosts = scanner.discover(target)
    
    print(f"Scan complete. Found hosts: {active_hosts}")

if __name__ == "__main__":
    main()