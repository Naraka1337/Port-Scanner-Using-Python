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
    threads = []  # Keep track of threads
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(targetIP, port))
        threads.append(thread)
        thread.start()

    # Join threads to ensure the script waits for all of them to finish
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    print("_NARAKA PORT SCANNER_\n")
    targetIP = input("Target IP: ")

    # The Banner
    print("_" * 50)
    print("Scanning Target: " + targetIP)
    print("Scanning Started at: " + str(datetime.now()))
    print("_" * 50)

    try:
        # Allow the user to specify the port range
        start_port = int(input("Enter the start port: "))
        end_port = int(input("Enter the end port: "))

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
