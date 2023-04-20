A= float(input("Enter first number: "))
B= float(input("Enter second number: "))
C = float(input("Enter third number: "))
 
if (A > B) and (A > C):
   largest = A
elif (B > A) and (B > C):
   largest = B
else:
   largest = C
 
print("The largest number is",largest)
##########output##########
#Enter first number: 4
#Enter second number: 6
#Enter third number: 8
#The largest number is 8.0
