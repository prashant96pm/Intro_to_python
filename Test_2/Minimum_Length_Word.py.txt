s=input().split()
l=[]
for i in s:
    l.append(len(i))
print(s[l.index(min(l))])