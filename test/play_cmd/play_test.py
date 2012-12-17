# References
#  http://docs.python.org/2/library/telnetlib.html
import sys
import telnetlib
import time

HOST = "localhost"
PORT = 4004
WAIT_TIME = 0.1

cmd_list=["help", "quit"] 

assert (len(sys.argv) == 2)

username = sys.argv[1]
tn = telnetlib.Telnet(HOST, PORT)
#tn1.set_debuglevel(7)
tn.read_until("name: ")
tn.write(username + "\n")
time.sleep(WAIT_TIME)

tn.read_until("): pick #")
tn.write("pick 1\n")
time.sleep(WAIT_TIME)

print tn.read_until("Your turn")
tn.write("play 7\n")
time.sleep(WAIT_TIME)

print "%s test PASSED!!!" % username
time.sleep(WAIT_TIME)

tn.write("quit\n")
