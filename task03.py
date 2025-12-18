n = int(input("Nechidan: "))
 
if n <= 15:
    for i in range(n, 15 + 1):
        print(i)
        
else:
    for i in range(n, 15 - 1, -1):
        print(i)    