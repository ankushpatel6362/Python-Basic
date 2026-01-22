n=int(input("enter n = "))
a=0
i=1
while i<=n:
  if (n==1 or n==0):  
    break
  if n%i==0:
        a+=1
  i+=1
if a==2:
   print(f"{n} : is prime no ") 
else:
   print(f"{n} : not a prime no")          