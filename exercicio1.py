'''
1-indentifique a maior sequencia de inteiros dentro de uma cadeia de características, levem em consideração sequências crescentes
'''

nums = [0, 15, 9, 27, 30, 3, 2, 5]
seq = []

for num in nums:
    if len(nums) > nums.index(num)+1 and num < nums[nums.index(num)+1]:
        seq.append([num, nums[nums.index(num)+1]])

print('\033[34m-=-= Sequencia -=-=\033[m')
print(f'\033[35m{seq}\033[m')
