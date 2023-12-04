with open("sample.txt", "r") as f:
    data = f.readlines()
total = 0
for line in data:
    nums = []
    num=0
    for letter in line:
        try:
            int(letter)
        except ValueError:
            pass
        else:
            nums.append(letter)
    num = int(nums[0]+nums[0]) if len(nums)==1 else int(nums[0]+nums[-1])
    total += num
    print(num, total)
