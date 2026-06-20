# main.py
from core.discovery.icmp import ICMPDiscovery
from core.scanner.tcp_scanner import TCPScanner

def main():
    print("--- Starting Network Vulnerability Scanner ---")
    
    # Instantiate our discovery worker
    scanner = ICMPDiscovery()
    
    # Give it a test target network
    target = "10.177.84.0/24"
    
    # Trigger the discovery phase
    active_hosts = scanner.discover(target)
    scanner = TCPScanner(max_threads=100)
    results = scanner.run(['10.177.84.52'], [22, 80])
    
    print(f"Scan complete. Found hosts: {results}")

if __name__ == "__main__":
    main()