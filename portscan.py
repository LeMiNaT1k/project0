import socket
import subprocess
import sys
from datetime import datetime

# Clear the screen
subprocess.call('clear', shell=True)

# Input
remoteServer    = raw_input("Enter a remote host to scan: ")
remoteServerIP  = socket.gethostbyname(remoteServer)

# Printing process
print "-" * 60
print "Please wait, scanning remote host", remoteServerIP
print "-" * 60

# Print time
t1 = datetime.now()

# It will scans all ports between 1 and 1024

# We also put in some error handling for catching errors

try:
    for port in range(1,1025):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print "Port {}: 	 Open".format(port)
        sock.close()

except KeyboardInterrupt:
    print "Exiting"
    sys.exit()

except socket.gaierror:
    print 'Hostname could not be resolved. Exiting'
    sys.exit()

except socket.error:
    print "No connection to server"
    sys.exit()

# Time stamp again
t2 = datetime.now()

# How long the script took to complete task
total =  t2 - t1

# Printing the information to screen
print 'Scanning Completed in: ', total
