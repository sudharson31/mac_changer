#CHANGING MAC_ADDRESSS
import subprocess
import optparse


def get_arguments():
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments)=parser.parse_args()

    if not options.interface:
        parser.error("[-] Please Specify a interface, use --help for more info")
    elif not options.new_mac:
        parser.error("[-] Please Specify a new mac, use --help for more info")

    return  options

def change_mac(interface,new_mac):
    print("[+] Changing The Mac Address For " + interface + " to " + new_mac)

    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])



options=get_arguments()
change_mac(options.interface, options.new_mac)




print("THNANKS FOR USING!!!!!!!")
