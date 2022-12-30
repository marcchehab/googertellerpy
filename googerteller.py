import requests, winsound, time
from random import choice
import scapy.all as scapy

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class DataAlerter:
    
    beeping = 0.0
    kill = False
    ips_found = []
    scapy_filter = ""

    def __init__(self):
            url = "https://raw.githubusercontent.com/berthubert/googerteller/main/goog-prefixes.txt"
            self.scapy_filter = "ip and ("+" or ".join(["net "+s.strip() for s in requests.get(url).text.splitlines()])+")"
            self.main()

    def main(self):
        try:
            scapy.sniff(iface="Ethernet", filter=self.scapy_filter, prn=self.handler, store=0)
        except KeyboardInterrupt:
            self.scapy_sniffer.stop()
            self.beeping = 1
            print(self.ips_found)
            self.kill = True

    def handler(self, packet):
        print(bcolors.__dict__[choice(dir(bcolors)[4:7])]+packet.summary()+bcolors.ENDC)
        ips = []
        if packet["Ethernet"].type == 2048: #IP
            ips = [packet[1].src, packet[1].dst]
        elif packet["Ethernet"].type == 2054: #ARP
            ips = [packet[1].psrc, packet[1].pdst]
        for ip in ips:
            if ip not in self.ips_found: self.ips_found.append(ip)
        if self.beeping + 1 < time.time() or self.beeping == 0:
            self.beeping = time.time()
            winsound.PlaySound(r"C:\Windows\Media\Windows Notify.wav", winsound.SND_ASYNC or winsound.SND_NOWAIT or winsound.SND_NOSTOP)

if __name__ == "__main__":
    da = DataAlerter()
