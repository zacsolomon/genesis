#!/usr/bin/python

import os
import sys
import subprocess
import time
import textwrap

def changemac():
	subprocess.call(["ifconfig","eth0","down"])
	subprocess.call(["macchanger","-A","wlan0"])
	subprocess.call(["ifconfig","eth0","up"])
	print("completed!")
	time.sleep(2)

def changehost(name):
	print("Changing hostname to %s")%(name)
	fhandler1 = open("/etc/hosts", 'w')
	hostinfo = """
		127.0.0.1	localhost %s
		::1		localhost ip6-localhost ip6-loopback
		fe00::0		ip6-localnet
		ff00::0		ip6-mcastprefix
		ff02::1		ip6-allnodes
		ff02::2		ip6-allrouters\n""" %(name)

	dedented_text = text.wrap.dedent(hostinfo).strip()
	fhandler1.write(dedented_text)
	fhandler1.close()

	fhandler2 = open("/etc/hostname", 'w')
	hostname = "%s\n"%(name)
	fhandler2.write(name)
	fhandler2.close()

def main():
	changemac():
	changehost(sys.argv[1])


if __name__ == "__main__":
	main()

# Add part about updating msf database
# Add part about launching beef framework
