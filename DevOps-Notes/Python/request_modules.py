# import requests
# response= requests.get("https://api.github.com/search/repositories",params={'q': 'requests+language:python'})
# repos= response.json()
# print repos['headers']['Content-Type']
# fist_repo= repos['items'][0]
# print fist_repo['name']

#REverse
# s= 'python'
# print ''.join(reversed(s))
# rs=''
# for i in range(len(s)):
# 	rs=s[i]+rs

# print rs

# l1=[1,2,3]
# l2=['a','b','c']
# d={}
# for k in l1:
# 	for v in l2:
# 		d[k]=v
# 		l2.remove(v)
# 		break
# print d
# print l2

# print zip(d.keys(),d.values())

# lambda function
max = lambda a, b : a if a > b else b
print max(10,20)

even = lambda a: a%2==0
print even(4)
#filter
l=[1,2,3,4,5]

print list(filter(lambda a: a%2==0,l))
