# main.py
from core.discovery.icmp import ICMPDiscovery
from core.scanner.tcp_scanner import TCPScanner

def main():
    print("--- Starting Network Vulnerability Scanner ---")
    test_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 443, 445, 3306, 3389]
    
    # Instantiate our discovery worker
    scanner = ICMPDiscovery()
    
    # Give it a test target network
    target = "10.18.48.88/24"
    
    # Trigger the discovery phase
    active_hosts = scanner.discover(target)
    scanner = TCPScanner(max_threads=100)
    results = scanner.run(active_hosts, test_ports)
    
    print(f"Scan complete. Found hosts: {results}")

if __name__ == "__main__":
    main()