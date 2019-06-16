# Program to identify if a character is an alphabet or not
a=input()
b=ord(a)
if((b>=65 and b<=90) or (b>=97 and b<=122)):
    print("Yes")
else:
    print("No")
