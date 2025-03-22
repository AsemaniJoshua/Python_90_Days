# Day 22-23: Building a Simple Port Scanner
# - Topics:
# - Learn how to scan open ports on a target machine using socket module.
# - Project:
# - Build a basic port scanner that checks if a port is open on a target server.


# Importing Libraries or Modules
import socket
import pyfiglet
import sys
from datetime import datetime
def port_scanner():
    try:
        ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
        print(ascii_banner)
        target = input("Enter the target IP address: ")
        targetIP = socket.gethostbyname(target)
        print("_"*50)
        print("Starting scan on host: ", targetIP, "at ", datetime.now())
        print("_"*50)
        for i in range(1, 65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.5)
            status = s.connect_ex((targetIP, i))
            if (status == 0):
                print("[*] Port", i, "is open")
            s.close()
            
    except KeyboardInterrupt:
        print("\n[*] Exiting program.")
        sys.exit()
        
    except socket.gaierror:
        print("\n[*] Hostname could not be resolved.")
        sys.exit()
        
    except socket.error:
        print("\n[*] Couldn't connect to server.")
        sys.exit()
        
        
port_scanner()