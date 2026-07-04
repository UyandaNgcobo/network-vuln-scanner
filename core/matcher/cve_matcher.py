import re
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

    def _match(self, banner, signatures):
        for key, value in signatures.items():
            match = re.search(value, banner)
        if match:
            print(f"{key}: {match.group(1)}")
                    
    def run(self, banners):
        cleaned_banners = []
        for item in banners:
            (ip, port, banner) = banners
            clean_text = self._match(banner, signatures)
            cleaned_banners.append(clean_text)
            
        return (ip, port, clean_text)