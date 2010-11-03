import cPickle

#This file is intended to add to and test the commands.ini file.
#Edit the commands dictionary.

PATH='commands.ini'

            #REGEX GOES HERE    :  RESPONSE GOES HERE
commands = {'THE SIX CODE \w+':'+pub Did someone ask for a bot?',
            'make me a sandwich':'+pub :grumbles and fashions a sandwich.\npage Pat=Jerk...'}

commandsFile = open(PATH,'wb')
cPickle.dump(commands,commandsFile)

commandsFile.close()


#this tests if the file loads properly
commandsFile = open(PATH,'r')
commands2 = cPickle.load(commandsFile)
commands2 = commands2.keys()
print commands2
commandsFile.close()
