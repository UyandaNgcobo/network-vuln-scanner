import re
import requests
import core.scanner.banner_grabber


signatures = {
    "ProFTPD" : {
                    "author" : "proftpd" ,
                    "regex" : r"ProFTPD/([\d+\.]+)"
                },
    "Apache" : {"vendor" : "apache", "regex" : r"Apache/([\d+\.]+)"},
    "mod_perl" : {"vendor" : "apache", "regex" :r"mod_perl/([\d+\.]+)"},
    "Perl" : {"vendor" : "perl", "regex" : r"Perl/v?([\d+\.]+)"},
    "OpenSSL" : {"vendor" : "openbsd", "regex" : r"OpenSSL/([\d+\.]+\w?)"},
    "PHP" :  {"vendor" : "apache", "regex" : r"PHP/([\d+\.]+)"},
    "OpenSSH" : {"vendor" : "apache", "regex" : r"OpenSSH_([\d+\.]+)"}
}


class CVEMatcher:
    def _init_(self):
        pass

    def _clean(self, banner, signatures):
        matches = []
        for key, value in signatures.items():
            match = re.search(value, banner)
            if match:
                matches.append((key, (match.group(1))))
        if matches:
            return matches
        
    def _match(self, app, ver, timeout=3.0):
        url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?cpeName=cpe:2.3:o:{app}:{ver}:1607&isVulnerable"
        response = requests.get(url)

        if response.status_code == 0:
            data = response.json()
            pass
        else:
            return None
                    
    def run(self, banners):
        for ip, port, banner in banners:
            clean_banners = self._clean(banner, signatures)
            print(f"\nIP: {ip}\nPort:{port}\nBanner: {clean_banners}")

            for app, ver in clean_banners:
                if not None:
                    self._match(banner)
                pass
            
        return (ip, port, clean_banners)