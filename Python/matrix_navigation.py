v=int(input())
t=[]
for i in range(v):
    p=input()
    p=p.split()
    for j in p:
            t.append(j)
z=int(input())
a=[]
for i in range(z):
    s=input()
    a.append(s)
x=1
for i in a:
    if(i=="RIGHT" and x%v!=0):
        x=x+1
    elif(i=="LEFT" and x%v!=1):
        x=x-1
    elif(i=="DOWN" and x<=(v*v)-v):
        x=x+v
    elif(i=="UP" and x>v):
        x=x-v
print(t[x-1])  
