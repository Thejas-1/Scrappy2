import re


with open('random.txt','r') as myfile:
    data = myfile.read().replace("alt=","..")
#with open('random.txt','r') as myfile:
#    data = myfile.read().replace("</html","blah")

#print (re.findall("Chiraag",data))
#print (re.split("..",data))
#print data

file = open('random.txt','r')
g = file.read()
i=0
a = []
for m in re.finditer('profile/',g):
    a.append(m.end())

for k in a:
    print k

print len(a)
