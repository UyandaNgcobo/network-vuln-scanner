import socket
import concurrent.futures

target_ip = ['10.177.84.52', '10.177.84.88'] #target ip from discovered hosts
target_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 443, 445, 3306, 3389] #checking if web server running

def scan_ports(ip, port):
    #1. build phone
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #dialing ipv4, using TCP

    #2. set timeout
    s.settimeout(1.0) #wait 1 sec and then give up

    #3. knock
    result = s.connect_ex((ip, port))

    #4. check results & throw phone
    if result == 0:
        return f"[+] Port {port} is OPEN!"
    else:     
        s.close() #throw phone away before loop restarts
        return None
    
def run_tcp_scan(target_ips, target_ports):

    #setting up slots for Futures
    futures = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:

        for host in target_ips:
            for port in target_ports:

                buzzer = executor.submit(scan_ports, host, port)
                futures.append(buzzer)

                for buzzer in concurrent.futures.as_completed(futures):
                    scan_result = buzzer.result()