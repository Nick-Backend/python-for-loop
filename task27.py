product_1 = int(input("1-Mahsulot narxi: "))
product_2 = int(input("2-Mahsulot narxi: "))
product_3 = int(input("3-Mahsulot narxi: "))
product_4 = int(input("4-Mahsulot narxi: "))

discount_1 = (product_1 -(product_1 * 10 / 100))
discount_2 = (product_2 -(product_2 * 10 / 100))
discount_3 = (product_3 -(product_3 * 10 / 100))
discount_4 = (product_4 -(product_4 * 10 / 100))

total = (discount_1 + discount_2 + discount_3 + discount_4)

print(total)

