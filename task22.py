tel_1 = int(input("1-telefon narxi: "))
tel_2 = int(input("2-telefon narxi: "))
tel_3 = int(input("3-telefon narxi: "))
tel_4 = int(input("4-telefon narxi: "))
tel_5 = int(input("5-telefon narxi: "))

max_price = max(tel_1, tel_2, tel_3, tel_4, tel_5)
min_price = min(tel_1, tel_2, tel_3, tel_4, tel_5)
avg_price = (max_price + min_price) / 2

print(avg_price)