import re
import requests
import core.scanner.banner_grabber


signatures = {
    "ProFTPD" : r"ProFTPD/([\d+\.]+)",
    "Apache" : r"Apache/([\d+\.]+)",
    "mod_perl" : r"mod_perl/([\d+\.]+)",
    "Perl" : r"Perl/v?([\d+\.]+)",
    "OpenSSL" : r"OpenSSL/([\d+\.]+\w?)",
    "PHP" :  r"PHP/([\d+\.]+)",
    "OpenSSH" : r"OpenSSH_([\d+\.]+)"
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
        
    def _match(self):
        pass
                    
    def run(self, banners):
        for ip, port, banner in banners:
            clean_banners = self._clean(banner, signatures)
            print(f"\nIP: {ip}\nPort:{port}\nBanner: {clean_banners}")
            
        return (ip, port, clean_banners)