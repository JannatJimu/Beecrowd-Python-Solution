code1, unit1, price1 = input().split()
unit1 = int(unit1)
price1 = float(price1)

code2,unit2,price2 = input().split()
unit2=int(unit2)
price2= float(price2)

total = unit1*price1 + unit2*price2
print(f"VALOR A PAGAR: R$ {total:.2f}")