n=0
f=open("Numbers.txt","w")
while n<4:
  f.write(input("please enter a number"))
  f.write(" ")
  n=n+1
f=open("Numbers.txt","r") 
print(f.read())
f.close()