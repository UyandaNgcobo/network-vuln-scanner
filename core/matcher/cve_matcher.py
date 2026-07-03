import re
import core.scanner.banner_grabber

signatures = {
    "ProFTPD" : r"([\d+\.]+)",
    "Apache" : r"([\d+\.]+)",
    "OpenSSL" : r"OpenSSL/([\d+\.]+)",
    "PHP" :  r"PHP/([\d+\.]+)",
    "OpenSSH" : r"OpenSSH_([\d+\.]+)"
}

class CVEMatcher:
    def _init_(self):
        pass

    def _match(banner, signatures):
        for value in signatures.values():
            match = re.search(value, banner)
        if match:
            print(match.group(1))
                

    def run(banners):
        pass