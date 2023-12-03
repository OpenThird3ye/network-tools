import subprocess
import csv
from datetime import datetime, timezone
'''import tkinter'''
''''from tkinter import messagebox'''

'''root = tkinter.Tk()'''
'''root.withdraw()'''
dt_now = datetime.now(tz=timezone.utc)




def ping(hostname):
    p = subprocess.Popen('ping ' + hostname + ' -n 1', stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    pingStatus = 'ok';

    for line in p.stdout:
        output = line.rstrip().decode('UTF-8')

        if (output.endswith('unreachable.')):
            # No route from the local system. Packets sent were never put on the wire.
            pingStatus = 'unreacheable'
            break
        elif (output.startswith('Ping request could not find host')):
            pingStatus = 'host_not_found'
            break
        if (output.startswith('Request timed out.')):
            # No Echo Reply messages were received within the default time of 1 second.
            pingStatus = 'timed_out'
            break
        # end if
    # endFor

    return pingStatus


# endDef


def printPingResult(hostname):
    statusOfPing = ping(hostname)

    if (statusOfPing == 'host_not_found'):
        #writeToFile('!server-not-found.txt', )
        print(hostname, ' server-not-found ')
        '''messagebox.showinfo(hostname, 'The device was not found on the network' )'''
    elif (statusOfPing ==  'unreacheable'):
        #writeToFile('!unreachable.txt', hostname)
        print(hostname, ' unreachable ')
    elif (statusOfPing == 'timed_out'):
        #writeToFile('!timed_out.txt', hostname)
        print(hostname, ' timed out ')
        '''messagebox.showwarning(hostname, 'The device was not found on the network')'''
    elif (statusOfPing == 'ok'):
        #writeToFile(hostname, 'OK' )
        print(dt_now, ' ok ', hostname)
    # endIf


# endPing


'''def writeToFile(filename, data):
    with open(filename, 'a') as output:
        output.write(data + '\n')
    # endWith
'''

# endDef


'''
servers.txt example
   vm8558
   host2
   server873
   google.com
'''
file = open('hosts.txt')

try:
    reader = csv.reader(file)
    for item in reader:
        printPingResult(item[0].strip())
    # endFor
finally:
    print()
    print("--Complete--")
    input("Press any key to exit")
    file.close()
# endTry
