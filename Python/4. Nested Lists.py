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
grades = []
for i in range(n):
    grades.append(data[i][1])
remover = min(grades)
while remover in grades:
    grades.remove(min(grades))
finder = min(grades)
names = []
for i in range(n):
    if finder == data[i][1]:
        names.append(data[i][0])
names.sort()
for i in names:
    print(i) 
