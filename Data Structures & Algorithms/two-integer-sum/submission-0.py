class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=[]
        for left in range(len(nums)):
            for right in range(left + 1, len(nums)):
                sum = nums[left]+nums[right]
                if target == sum:
                    l.extend([left,right])
                    l.sort()
                    return l
        return l
