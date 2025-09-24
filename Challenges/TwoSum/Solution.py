def two_sum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in nums and nums.index(complement) != i:
            return [i, nums.index(complement)]

print(two_sum([2, 7, 11, 15], 9))  # saída: [0, 1]
print(two_sum([3, 2, 4], 6))  # saída: [1, 2]
print(two_sum([3, 3], 6))  # saída: [0, 1]
