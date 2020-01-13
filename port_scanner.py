#!/bin/python

import sys 
import socket 
from datetime import datetime


# Define input
if len(sys.argv) == 2: 

    target = socket.gethostbyname(sys.argv[1])

else: 

    print("Invalid amount of arguments")
    print("Ex. python3 port_scanner.py 192.0.0.1")
    sys.exit()

# Banner

print("#" * 50)
print("Scanning " + target)
print("Scan started at " + str( datetime.now() ))
print("#" * 50)

try: 
    for port in range(50, 85):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = s.connect_ex((target,port))
        if result == 0: 
            print( "Port {} is open".format(port) )

        s.close()

except KeyboardInterrupt: 
    print("Error, Exiting...")
    sys.exit()

except socket.gaierror: 
    print("Hostname could not be resolved to ip")
    sys.exit()

except socket.error:
    print("Could not connect to target")
    sys.exit()