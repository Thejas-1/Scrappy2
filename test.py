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
for m in re.finditer('data-account-key',g):
    a.append(m.end())

#for k in a:
#    print k
s = []
print a[1]

file.seek(a[0]+2)

i=a[0]+1
ch = file.read(1)
while (ch!='\"'):
    i=i+1
    file.seek(i)
    ch = file.read(1)
    if ch=='\"':
        break
    else:
        s.append(ch)
        str1 = ''.join(s)
print str1

file.close()


