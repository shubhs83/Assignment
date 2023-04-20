i=int(input("Enter the number :")) 
columns=10
for j in range(1,columns+1):
   table=i*j
   print("{:2d} ".format(table),end='')

   #########output#########
   #Enter the number : 9
#9
#> 
#9 18 27 36 45 54 63 72 81 90 >