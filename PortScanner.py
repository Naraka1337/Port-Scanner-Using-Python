import sys
import socket
from datetime import datetime

print("_NARAKA PORT SCANNER_\n")
targetIP = input("Target IP: ")

# The Banner
print("_" * 50)
print("Scanning Target: " + targetIP)
print("Scanning Started at: " + str(datetime.now()))
print("_" * 50)

try:
    # Scan Every Port
    for port in range(2, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        # Return Open Port
        openPort = s.connect_ex((targetIP, port))
        if openPort == 0:
            print("[*] Port {} is OPEN".format(port))
        s.close()

except KeyboardInterrupt:
    print("\n Exiting... Bye Bye!")
    sys.exit()

except socket.gaierror:
    print("\n Hostname could not be resolved. Exiting...")
    sys.exit()

except socket.error:
    print("\n Couldn't connect to server. Exiting...")
    sys.exit()

print("\nScan Complete :)")