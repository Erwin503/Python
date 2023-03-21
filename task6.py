a = input()
l = len(a)
res = ''
for i in range(l - 1, -1, -1):
    res = res + a[i]
print(res)