n = int(input())
data = []
for i in range(n):
    temp = []
    for j in range(2):
        var = input()
        if var.isdigit():
            temp.insert(j, int(var))
        else:
            temp.insert(j, var)
    data.append(temp)
print(data)
