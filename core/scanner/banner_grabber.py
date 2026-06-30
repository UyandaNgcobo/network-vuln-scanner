import socket
import concurrent.futures

class BannerGrabber:
    def __init__(self):
        pass

    def _probe(self, s, ip, port):

        probe = 'GET / HTTP/1.1\r\n\r\n'
        s.sendall(probe.encode('utf-8'))
        raw_p_data = s.recv(1024)
        clean_text = raw_p_data.decode('utf-8')
        return clean_text

        #actuall banner grabbing
    def _grab_banner(self, ip, port):

        #build the phone
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #dialing ipv4, using TCP

        #2. set timeout
        s.settimeout(self.timeout) #wait x seconds and then give up

        #3. knock
        result = s.connect_ex((ip, port))

        #probe: GET / HTTP/1.1\r\n\r\n
        #before sending HTPP, use .encode('utf-8')
        #when recieving bytes, use .decode('utf-8')
         #active ports
        if port == 80 or port == 443:
            banner = self._probe(s, ip, port)
        else:
            raw_a_data = s.recv(1024)
            raw_a_data.decode('utf-8')

        #& throw phone
        s.close()

        pass

    def run(self,target_hosts):
        print("[*] Grabbing banners...")
        for ip, port in target_hosts:
            self._grab_banner(ip, port)