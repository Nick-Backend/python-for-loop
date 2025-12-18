num = int(input("-> "))
toq_yigindi = 0
juft_yigindi = 0

for i in range(2, num + 1, 2):
    juft_yigindi += i
    
print(f"Juft son: {juft_yigindi}")

for i in range(1, num + 1, 2):
    toq_yigindi += i

print(f"Toq son: {toq_yigindi}")   
