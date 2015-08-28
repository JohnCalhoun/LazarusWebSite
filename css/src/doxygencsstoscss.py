#!/usr/bin/python
import re
import string

css=open("doxygen.css",'r')
contents=css.read()
css.seek(0)
contentsnew=css.readlines();
output=[]
################colors extract
colorsregex=re.compile(r'.*(cyan|#\w\w\w\w\w\w |#\w\w\w\w\w\w;|#\w\w\w\w\w\w\n|rgba\(.*\)).*')
colorsfound=colorsregex.findall(contents)

inc=0
colors=[] 
for color in set(colorsfound):
	temp=color.replace(";","");
	temp=temp.replace("\n","");
	colors.append( ["$color_"+str(inc),temp])
	inc=inc+1

variables=[]
for c in colors:
	variables.append(c[0]+": "+c[1]+"; \n")

for v in variables:
	output.insert(0,v)

for line in contentsnew:
	temp=line
	for c in colors:
		temp=temp.replace(c[1],c[0])
	output.append(temp)

################images extract
imgregex=re.compile(r'.*(\'.*\.png\').*')
imgfound=imgregex.findall(contents)

inc=0
imgs=[] 
for img in set(imgfound):
	imgs.append( ["$img_"+str(inc),img.replace(";","") ])
	inc=inc+1

im_variables=[]
for i in imgs:
	im_variables.append(i[0]+": "+i[1]+"; \n")

temp_out=[]
for line in output:
	temp=line
	for i in imgs:
		temp=temp.replace(i[1],i[0])
	temp_out.append(temp)
output=temp_out

for v in im_variables:
	output.insert(0,v)

##write out
outputfile=open("doxygen.scss",'w')
outputfile.write("".join(output))



#print "".join(contentsnew)
