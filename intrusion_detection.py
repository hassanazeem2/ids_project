from scapy.all import sniff
import time
from colorama import Fore, Style, init

init(autoreset=True)

class IntrusionDetectionSystem:
    def __init__(self):
        pass

    def print_green(self, text):
        print(Fore.GREEN + text + Style.RESET_ALL)

    def print_red(self, text):
        print(Fore.RED + text + Style.RESET_ALL)

    def detect_intrusion(self, packet):
        self.print_red(packet.summary())
        time.sleep(1)

    def wait_for_space(self):
        input("Press ENTER to start...")

    def run(self):
        self.print_green("▪   ▐ ▄ ▄▄▄▄▄▄▄▄  ▄• ▄▌·▄▄▄▄  ▄▄▄ .▄▄▄  ")
        self.print_green("██ •█▌▐█•██  ▀▄ █·█▪██▌██▪ ██ ▀▄.▀·▀▄ █·")
        self.print_green("▐█·▐█▐▐▌ ▐█.▪▐▀▀▄ █▌▐█▌▐█· ▐█▌▐▀▀▪▄▐▀▀▄ ")
        self.print_green("▐█▌██▐█▌ ▐█▌·▐█•█▌▐█▄█▌██. ██ ▐█▄▄▌▐█•█▌")
        self.print_green("▀▀▀▀▀ █▪ ▀▀▀ .▀  ▀ ▀▀▀ ▀▀▀▀▀•  ▀▀▀ .▀  ▀                 by Hassan Azeem")
        self.wait_for_space()
        self.print_green("Starting Intrusion Detection System...")
        sniff(prn=self.detect_intrusion, store=0, timeout=10, count=50)

# Main entry point
if __name__ == "__main__":
    ids = IntrusionDetectionSystem()
    ids.run()
