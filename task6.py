a = input()
l = len(a) - 1
res = ''
while l > -1:
    res = res + a[l]
    l -= 1
print(res)