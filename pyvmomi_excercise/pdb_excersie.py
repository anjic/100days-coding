# import pdb

# pdb.set_trace()
def loop(k):
    print "K:",k
    a = []
    for i in k:
        a.sort(i)
    return a 

print "sd :",loop([10,5,6,7,9])