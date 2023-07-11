class Solution(object):
    def removeDuplicates(self, nums):
        n = len(nums)
        i = 0

        while(i < n-1):
            if nums[i] == nums[i+1]:
                nums.pop(i)
                n -= 1
                i -= 1
            
            i += 1
