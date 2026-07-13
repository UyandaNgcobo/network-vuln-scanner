import re
import requests
import time
import core.scanner.banner_grabber


signatures = {
    "ProFTPD" : {
                    "author" : "proftpd" ,
                    "regex" : r"ProFTPD/([\d+\.]+)"
                },
    "http_server" : {"vendor" : "apache", "regex" : r"Apache/([\d+\.]+)"},
    "mod_perl" : {"vendor" : "modperl", "regex" :r"mod_perl/([\d+\.]+)"},
    "Perl" : {"vendor" : "perl", "regex" : r"Perl/v?([\d+\.]+)"},
    "OpenSSL" : {"vendor" : "openssl", "regex" : r"OpenSSL/([\d+\.]+\w?)"},
    "PHP" :  {"vendor" : "php", "regex" : r"PHP/([\d+\.]+)"},
    "OpenSSH" : {"vendor" : "openbsd", "regex" : r"OpenSSH_([\d+\.]+)"}
}


class CVEMatcher:
    def _init_(self):
        pass

    def _clean(self, banner, signatures):
        print("[*] Cleaning banners...\n")
        #list incase there's more than 1 software matched
        matches = []
        for key, value in signatures.items():
            match = re.search(value["regex"], banner)
            if match:
                #appends app, vendor and version
                matches.append((key, value["vendor"], (match.group(1))))
            else:
                continue

        time.sleep(1)
        if matches:
            print(f"[+] Recognised Banners: {matches}")
            return matches
        else:
            print("[-] Banner not recognised.\n")
        
    def _match(self, clean_banner):
        print("[*] Matching product against database...\n")
        app, vendor, ver = clean_banner
    
        url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?cpeName=cpe:2.3:a:{vendor}:{app.lower()}:{ver}:*:*:*:*:*:*:*"

        try:
            print("[+] Getting url....\n")
            response = requests.get(url)
            if response.status_code == 200:
                print("Got it!\n")
                data = response.json()
                print(data["vulnerabilities"][0]["cve"][0]["vulnStatus"])
            else:
                print("[-] Did not get it!\n")
                return None
        except Exception as e:
            print(f"Error: {e}\n")
                
    def run(self, banners):
        timeout=5.0
        clean_banners = []
        #extracting app, vendor, ver in banners
        for ip, port, banner in banners:
            print(f"IP: {ip}\nPort: {port}")
            clean_banners.append((ip, port, self._clean(banner, signatures)))
            print("----------------------------------------------------------------------------------------------\n")
        
        print("\n[+] --- Cleaning is done! ---\n")
        print(f"Clean banners: {clean_banners}\n")
        
        for clean_banner in clean_banners:
    
            if clean_banner:
                print("\n ------ I'm here! ------ \n")
                print(f"Banner to work on right now: {clean_banner}")
                app, vendor, ver = clean_banner
                print(f"App:{app}\nVendor: {vendor}\nVersion:{ver}")
                self._match(clean_banner)
                time.sleep(timeout)
            else:
                continue
        

        