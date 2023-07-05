# javohir
a = int(input("raqam kiriting:"))
if a == 0:
    print("bu son nolga teng")
elif a > 0 and a % 2 ==0:
    print("bu musbat juft son")
elif a > 0 and a % 2 == 1:
    print("bu musbat toq son")
elif a < 0 and abs(a) % 2 == 0:
    print("bu manfiy juft son")
elif a < 0 and abs(a) % 2 == 1:
    print("bu manfiy toq son")
