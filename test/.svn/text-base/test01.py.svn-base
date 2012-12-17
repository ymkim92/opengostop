# References
#  http://jimmyg.org/blog/2009/working-with-python-subprocess.html
import subprocess
import shlex
import time

username1="01"
username2="02"
username3="03"
cmd_list=["help", "quit"] 

#args = shlex.split("/usr/bin/python multi_server.py")
#fd_server = subprocess.Popen(args)
#time.sleep(1)
args = shlex.split("telnet localhost 4004")
user1 = subprocess.Popen(args, shell=False, 
						 stdin=subprocess.PIPE, 
						 stdout=subprocess.PIPE, 
						 stderr=subprocess.PIPE)

print "2..."
time.sleep(.1)
while True:
	output = user1.stdout.readline()
	if not output:
		break
	print output
output = user1.stdout.readline()
print output
user1.stdin.write(username1)
for command in cmd_list:
	user1.stdin.write(command)
	time.sleep(.1)
	output = user1.stdout.readlines()
	print output
