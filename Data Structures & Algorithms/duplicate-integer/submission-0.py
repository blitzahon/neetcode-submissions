class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        flag = False
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i+1]:
                flag = True
                break
            
        return flag
