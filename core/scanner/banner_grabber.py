import socket
import concurrent.futures

class BannerGrabber:
    def __init__(self):
        pass

    def _probe(s, host):

        probe = 'GET / HTTP/1.1\r\n\r\n'
        s.sendall(probe.encode('utf-8'))
        raw_p_data = s.recv(1024)
        clean_text = raw_p_data.decode('utf-8')

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
        raw_a_data = s.recv(1024)
        raw_a_data.decode('utf-8')
       

        #passive  ports
       

        #& throw phone
        s.close()

        pass

    def run(target_hosts):
        print("[*] Grabbing banners...")
        pass