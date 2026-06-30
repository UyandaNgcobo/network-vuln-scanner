# main.py
from core.discovery.icmp import ICMPDiscovery
from core.scanner.tcp_scanner import TCPScanner
from core.scanner.banner_grabber import BannerGrabber

def main():
    print("--- Starting Network Vulnerability Scanner ---")
    test_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 443, 445, 3306, 3389]
    
    # Instantiate our discovery worker
    icmp_scanner = ICMPDiscovery()
    
    # Give it a test target network
    target = "10.18.48.88/24"
    
    # Trigger the discovery phase
    active_hosts = icmp_scanner.discover(target)
    tcp_scanner = TCPScanner(max_threads=100)

    tcp_results = tcp_scanner.run(active_hosts, test_ports)
    banner_grabber = BannerGrabber.run(tcp_scanner)
    
    print(f"Scan complete. Found hosts: {tcp_results}")

if __name__ == "__main__":
    main()