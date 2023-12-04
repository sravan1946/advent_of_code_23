# FIXME: this is not working
from icecream import ic
from copy import deepcopy
with open("testsample2.txt", "r") as f:
    data = f.readlines()
table: dict[str, str] = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
total = 0
for line in data:
    nums: list[str] = []
    l = line
    line = deepcopy(line.strip())
    while line:
        # check for all the numbers
        for i in range(1, 10):
            ic(line, nums, i)
            if line.endswith(str(i)):
                nums.append(str(i))
                break

        # check for all the words
        for i in table:
            # ic(i, line, line.endswith(i))
            if line.endswith(i):
                nums.append(table[i])
                line = line[:-len(i)]
                break
        else:
            line = line[:-1]  

    nums = nums[::-1]
    num = int(nums[0]+nums[-1])
    total += num
    ic(l, nums,num, total)
