n = int(input())
data = {}
avar = 0
for i in range(n):
    name, *val = input().split()
    scores = list(map(float, val))
    data[name] = scores
select = input()
for i, j in data.items():
    if select == i:
        avar = sum(j) / len(j)
print('%.2f' %avar) 