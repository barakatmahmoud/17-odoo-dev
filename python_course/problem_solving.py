### List Comprehensions
x = int(input("Please enter a number"))
y = int(input("Please enter a number"))
z = int(input("Please enter a number"))
n = int(input("Please enter a number"))
result = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k != n:
                result.append([i,j,k])
print(result)