import socket
import concurrent.futures

class BannerGrabber:
    def __init__(self, max_workers=50, timeout=2.0):
        self.timeout = timeout
        self.max_workers = max_workers

    def _probe(self, s, ip, port):

        probe = 'GET / HTTP/1.1\r\n\r\n'
        s.sendall(probe.encode('utf-8'))
        raw_p_data = s.recv(1024)
        clean_text = raw_p_data.decode('utf-8', errors='ignore')
        return clean_text

        #actuall banner grabbing
    def _grab_banner(self, ip, port):

        #build the phone
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #dialing ipv4, using TCP

        #2. set timeout
        s.settimeout(self.timeout) #wait x seconds and then give up

        try:
            s.connect((ip, port))

            if port == 80 or port == 443:
                banner = self._probe(s, ip, port)
            else:
                raw_a_data = s.recv(1024)
                banner = raw_a_data.decode('utf-8')
            s.close()

            return (ip, port, banner.strip())
        
        except Exception as e:
            return (ip, port, "No Banner / Connection Failed")
        
    def run(self, target_hosts):
        print("[*] Grabbing banners...\n")

        futures = []
        banners = []

        with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
            for ip, port in target_hosts:
                buzzer = executor.submit(self._grab_banner, ip, port)
                futures.append(buzzer)
            
            for buzzer in concurrent.futures.as_completed(futures):
                grabbing_result = buzzer.result()

                if grabbing_result is not None:
                    result_banner = grabbing_result
                    banners.append((grabbing_result))

                    print(f"\nBanner: {result_banner}\n\n")
        
        return banners