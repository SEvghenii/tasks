
def minturns(nums):
    tests = list(range(min(nums), max(nums) + 1))
    turns = []
    n = 0
    for x in tests:
        for i in nums:
            if i != x:
                n += abs(x-i)
                i = i+(x-i)
        turns.insert(i, n)
        n = 0
    return min(turns)


filename = str(input('ведите файл-источник: '))
file1 = open(f"{filename}", "r")
testlist = list()
while True:
    line = file1.readline()
    if not line:
        break
    testlist.append(int(line.strip()))
file1.close

x = minturns(testlist)
print(x)
