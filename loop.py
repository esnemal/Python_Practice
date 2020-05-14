number = [4,56,43,78,90,43,76,45,98,00,34,56,77,7,8]

for x in number:
    if x == 77:
        break
    if x % 2 == 1:
        continue
    print(x)

