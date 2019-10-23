l =[1,2,3,4,6]
# print len(l)

s = "Geeks for geeks"
print reversed(s)
for i in s.split(" "):
    print i
    j=''
    for k in i: 
        print k+j
        print"$$$$$$$$$$$$$$$$$$"
        print j+k
    print j


def reverse(si):
  str = ""
  for i in s:
    str = i + str
  return str

ks = "Geeks for geeks"
print reverse(ks)