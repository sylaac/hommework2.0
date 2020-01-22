name=input('what is your name ?')
print("hello", name)
choice = "yes"
while "yes" == choice:
 a=input('give me the real number you want to devise')
 b=input('give me the divisor')
 a=float(a)
 b=float(b)
 c=a%b
 if c < b/2 :
     d=int(a/b)
 else :
     d=int(a/b+1)
 print("the rounded division is",d)
 choice=input("tape yes if you want to do a new division")

