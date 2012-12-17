# References
#  http://docs.python.org/2/library/telnetlib.html
import sys
import telnetlib
import time

HOST = "localhost"
PORT = 4004

username1="01"
username2="02"
username3="03"
cmd_list=["help", "quit"] 

tn1 = telnetlib.Telnet(HOST, PORT)
#tn1.set_debuglevel(7)
tn1.read_until("name: ")
tn1.write(username1 + "\n")
time.sleep(.1)

tn2 = telnetlib.Telnet(HOST, PORT)
#tn2.set_debuglevel(7)
tn2.read_until("name: ")
tn2.write(username2 + "\n")
time.sleep(.1)

tn3 = telnetlib.Telnet(HOST, PORT)
#tn3.set_debuglevel(7)
tn3.read_until("name: ")
tn3.write(username3 + "\n")
time.sleep(.1)
tn1.write("pick 4\n")
time.sleep(1.1)
tn2.write("pick 3\n")
time.sleep(1.1)
tn3.write("pick 2\n")
time.sleep(1.1)
tn3.write("who\n")
time.sleep(1.1)
print tn3.read_until("03 picks", 2)
print "test PASSED!!!"
time.sleep(2.1)



tn1.write("quit\n")
tn2.write("quit\n")
tn3.write("quit\n")