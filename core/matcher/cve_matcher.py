import re

signatures = {
    "ProFTPD" : r"([\d+\.]+)",
    "Apache" : r"([\d+\.]+)",
    "OpenSSL" : r"OpenSSL/([\d+\.]+)",
    "PHP" :  r"PHP/([\d+\.]+)",
    "OpenSSH" : r"OpenSSH_([\d+\.]+)"
}