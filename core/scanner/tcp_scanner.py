import socket
import concurrent.futures

target_ip = ['10.177.84.52', '10.177.84.88'] #target ip from discovered hosts
target_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 443, 445, 3306, 3389] #checking if web server running


class TCPScanner:
    def __init__(self, max_threads=50, timeout=1.0):
        #configuration
        self.max_threads = max_threads
        self.timeout = timeout

    def _scan_port(self, ip, port):
        # HELPER, handles actual socket connection
        #1. build phone
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #dialing ipv4, using TCP

        #2. set timeout
        s.settimeout(self.timeout) #wait x seconds and then give up

        #3. knock
        result = s.connect_ex((ip, port))

        #& throw phone
        s.close()

        #4. check results
        if result == 0:
            return (ip, port)
        return None
    
    def run(self, target_ips, target_ports):
        print(f"[*] Starting TCP Port Scan...")

        #setting up slots for Futures
        futures = []
        active_services = [] #to hold successful hits

        with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:

            for host in target_ips:
                for port in target_ports:

                    buzzer = executor.submit(self._scan_port, host, port)
                    futures.append(buzzer)
    
            for buzzer in concurrent.futures.as_completed(futures):
                scan_result = buzzer.result()
                
                if scan_result is not None:
                    active_services.append(scan_result)

                    print(f"[+] {scan_result[0]} Port {scan_result[1]} is OPEN!")
            
        return active_services


# if __name__ == "__main__":
#     # Testing data locally
#     test_ips = ['10.177.84.52', '10.177.84.88'] 
#     test_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 443, 445, 3306, 3389]
    
#     run_tcp_scan(test_ips, test_ports)