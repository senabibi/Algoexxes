def can_partition_three_ways(nums):
    total_sum = sum(nums)
    if total_sum % 3 != 0:
        return 0  

    target_sum = total_sum // 3
    subsets = [0] * 3

    def backtrack(index):
        if index == len(nums):
            return subsets[0] == subsets[1] == target_sum

        for i in range(3):
            if subsets[i] + nums[index] <= target_sum:
                subsets[i] += nums[index]
                if backtrack(index + 1):
                    return True
                subsets[i] -= nums[index]

        return False

    return 1 if backtrack(0) else 0


n = int(input(" "))
nums = list(map(int, input(" ").split()))

print(can_partition_three_ways(nums))
