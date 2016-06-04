import getpass
import sys
import cPickle
import telnetlib

HOST = "" #hostname to connect to
PORT = #port to connect to

user = raw_input("username: ");
passw = getpass.getpass();

tn = telnetlib.Telnet(HOST,PORT)
#logging in
tn.write("connect " + user + " " + passw + "\n");

def command(tn, cmd):
	tn.write(cmd+'\n');

def pub(tn, cmd):
	command(tn,"+pub " + cmd)

commandsFile = open('commands.ini', 'rb')
commands = cPickle.load(commandsFile) 
commandsFile.close()

replies = commands.values()
commands = commands.keys()

print replies
print commands

while 1:
	retval = tn.expect(commands)
	if retval[0] != -1:
		#http://docs.python.org/library/re.html#re.MatchObject
		command(tn,replies[retval[0]]);
		#debug
		print retval[2]
