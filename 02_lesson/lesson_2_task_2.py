def is_year_leap(year):
     
     return True if (year) % 4 == 0 else False 

num = int(input("ГОД:  "))

result = is_year_leap(num)

print(f"Делится ли на 4 {num}? - {result}")

print(f"ГОД {num} : {result}")

print("Если число года частное без остатка, год високосный и наоборот")
