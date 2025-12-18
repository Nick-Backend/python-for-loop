narx_1 = int(input("-> "))
narx_2 = int(input("-> "))
narx_3 = int(input("-> "))
narx_4 = int(input("-> "))
narx_5 = int(input("-> "))


yigindi = 0

if narx_1 % 5 == 0:
    yigindi += narx_1
           
if narx_2 % 5 == 0:
    yigindi += narx_2
    
if narx_3 % 5 == 0:
    yigindi += narx_3
    
if narx_4 % 5 == 0:
    yigindi += narx_4
          
if narx_5 % 5 == 0:
    yigindi += narx_5
 
print(yigindi)        

