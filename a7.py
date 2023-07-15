x = range(120,1200)
numbers = []

for n in x:   
    numbers.append(n)    
    
print(sum(numbers))
print(max(numbers)-min(numbers))
print(len(numbers))
print(numbers[:20],numbers[400:420],numbers[-1:-21:-1])