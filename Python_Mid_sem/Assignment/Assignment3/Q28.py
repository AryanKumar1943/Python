s="python"
l=[]
for i in s:
    if i=='z':
        l.append('a')
    aski=ord(i)
    aski=aski+1
    l.append(chr(aski))
res="".join(l)
print(res)