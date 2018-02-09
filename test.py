import re

def substract(a, b):                              
    return "".join(a.rsplit(b))
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
str1 = ''
names = []
for k in a:
    i = k+1
    ch = file.read(1)
    str1 = ''
    while (ch!='\"'):
        i=i+1
        file.seek(i)
        ch = file.read(1)
        if ch=='\"':
            break
        else:
            s.append(ch)
            str1 = ''.join(s)
    names.append(str1)

length = len(names)-1
usernames = []
while length!=0:
    usernames.append(names[length].replace(names[length-1],""))
    length=length-1

usernames.append(names[0])
print usernames
#print names
#print len(a)

file.close()

links = []
str = "https://www.researchgate.net/profile/"
length = len(usernames)

for i in range(0,length):
    links.append(str+usernames[i])

print links
#print "lamp, bag, mirror".replace("bag,","")


