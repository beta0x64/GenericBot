import getpass
import sys
import telnetlib

HOST = "66.234.205.2"
PORT = 4201

user = raw_input("username: ");
passw = getpass.getpass();

tn = telnetlib.Telnet(HOST,PORT)
#logging in
tn.write("connect " + user + " " + passw + "\n");
print tn.read_eager()

def command(tn, cmd):
	tn.write(cmd+'\n');

def pub(tn, cmd):
	command(tn,"+pub " + cmd)

commands = ["THE SIX CODE WORDS","make me a sandwich"]

while 1:
	retval = tn.expect(commands)
	if retval[0] != -1:
		if retval[1].group(0) == commands[0]:
			pub(tn, "Did someone ask for a bot?")
		elif retval[1].group(0) == commands[1]:
			pub(tn, ":grumbles and fashions a sandwich\n+pub Jerk...")
	

