import sys
import socket
from datetime import datetime
import threading

# Function to scan a single port
def scan_port(targetIP, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        openPort = s.connect_ex((targetIP, port))
        if openPort == 0:
            print(f"[*] Port {port} is OPEN")
        s.close()
    except socket.error:
        pass  # Silently ignore errors for closed ports

# Function to manage multithreading
def scan_ports(targetIP, start_port, end_port):
    for port in range(start_port, end_port):
        thread = threading.Thread(target=scan_port, args=(targetIP, port))
        thread.start()

if __name__ == "__main__":
    print("_NARAKA PORT SCANNER_\n")
    targetIP = input("Target IP: ")

    # The Banner
    print("_" * 50)
    print("Scanning Target: " + targetIP)
    print("Scanning Started at: " + str(datetime.now()))
    print("_" * 50)

    try:
        # Range of ports to scan (1-1024 are the most common ports)
        start_port = 1
        end_port = 1024

        # Start multithreading scan
        scan_ports(targetIP, start_port, end_port)

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
