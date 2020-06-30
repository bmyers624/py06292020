#!/usr/bin/env python3
"""Alta3 Research || Author b.myers624@gmail.com"""

# funtion to push commands
def commandpush(devicecmd): # devicecmd==list
    for coffeetime in devicecmd.keys():
        print('Handshaking. .. ... connecting with ' + coffeetime )
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[coffeetime]:
            print('Attempting to send command --> ' + mycmds )
            # we'll learn to write code that sends cmds to device here

# start of main script
def main():
    work2do = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]} 
    # data that replaces data stored in file

    print("Welcome to the network device command pusher")

    print("\nData set found\n")

    # run
    commandpush(work2do)

# call main function
main()

