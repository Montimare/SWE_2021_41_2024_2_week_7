from typing import List

def twoSums(nums: List[int], target: int) -> List[int]:
    # Try all possible combinations of two numbers
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                # Solution found return indices
                return [i, j]
    return []

# print(twoSums([3,2,4], 6))