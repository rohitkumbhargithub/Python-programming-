#Alpabatic(al) pattern using for loop

n=int(input("Enter the Character A to Z(65 to 90): "))
for i in range(0,5):
   for j in range(0,i+1):
     al=chr(n)
     print(al, end=' ')
     n+=1
   print()
