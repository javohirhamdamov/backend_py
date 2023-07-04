# javohir
a = int(input("a="))
if a == 0:
    print("son nolga teng")
elif a > 0 and a % 2 ==0:
    print("musbat juft son")
elif a > 0 and a % 2 == 1:
    print("musbat toq son")
elif a<0 and abs(a) % 2 == 0:
    print("manfiy juft son")
else:
    print("manfiy toq son")