# #sonni faktaryali
# a = int(input())
# i = 0
# n = 1
# while a-i>0:
#     n = n*(a-i)
#     i+=1
# print(n)

# # yulduzcha
# n = int(input())
# for i in range(n):
#     print("*"*(n-i))
# ------------------
# n = int(input())
# i = 0
# while n - i > 0:
#     print("*" * (n - i)) 
#     i += 1
    
#list while for amaliy
n_list = [32,4,12,3,7,23,21]
for n in n_list:
    if n%3 != 0 and n%7 != 0:
        print(n)
    else:
        break
