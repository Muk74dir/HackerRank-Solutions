n = int(input())
data = []
for i in range(n):
    temp = []
    for j in range(2):
        var = input()
        try:
            temp.append(float(var))
        except:
            temp.append(var)
    data.append(temp)
print(data)
