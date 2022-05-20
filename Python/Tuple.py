n = int(input())
val = input().split(" ")
result = []
for i in range(n):
    result.append(int(val[i]))
print(result)
print(hash(tuple(result)))