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
        
    def _match(self, app, vendor, ver):
        """
        - The ip, port and clean banner is passed in here as a tuple.
        - i.e, (ip, port, [(banner), (banner)])
        - The banner gets unpacked and has its data fitted into the API parameters
        - i.e, app, vendor, ver = (banner)
        - try-catch attempts to get data from database via API and checks response and then formats it into JSON.
        """
        print("[*] Matching product against database...\n")
        #unpacking ip, port and clean banner
        url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?cpeName=cpe:2.3:a:{vendor}:{app.lower()}:{ver}:*:*:*:*:*:*:*"

        try:
            print("[*] Getting url....\n")
            response = requests.get(url)
            if response.status_code == 200:
                print("Got it!\n")
                data = response.json()
                if len(data["vulnerabilities"][0]) > 0:
                    vuln_data = data["vulnerabilities"][0]["cve"]
                    cve_id = vuln_data["id"]
                    vuln_status = vuln_data["vulnStatus"]
                    return cve_id, vuln_status
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
        
        #seperating ip, port and banner
        for ip, port, recognised_list in clean_banners:
            print(f"IP: {ip}\nPort: {port}")

            if recognised_list is not None:

                #grabbing a banner at a time
                for banner in recognised_list: 

                    #seperating app, vendor and version inside banner
                    app, vendor, ver = banner
                    print(f"App:{app}\nVendor: {vendor}\nVersion:{ver}")
                    self._match(app, vendor, ver)
                    time.sleep(timeout)
                else:
                    continue
            print("----------------------------------------------------------------------------------------------\n")
        

        