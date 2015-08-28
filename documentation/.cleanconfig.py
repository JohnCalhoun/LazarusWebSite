#!/usr/bin/python
import re
import string

config=open("config",'r')
contents=config.readlines();
config.close()
output=[]
#remofe all comments and empty lines
reg=re.compile(r'#.*|\n')

for line in contents:
	if reg.match(line)==None:
		output.append(line)

#write out
outputfile=open("config",'w')
outputfile.write("".join(output))

