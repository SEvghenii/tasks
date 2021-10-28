n = int(input('Введите число: '))
m = int(input('Введите число: '))
nums = list(range(1, n + 1))

c = (nums[m - 1:] + nums[:m - 1])
d = list()
z = ''
d.append(nums[0])
while c[0] != d[0]:
    d.append(c[0])
    c = (c[m - 1:] + c[:m - 1])
for i in range(len(d)):
    z += str(d[i])
print(int(z))
