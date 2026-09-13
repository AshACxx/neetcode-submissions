class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)

        res = nums[0]
        l, r = 0, len(nums) - 1


        while l <= r:
            m = l + ((r - l) // 2)
            if num[m] < num[r]:
                r = m
            else:
                l = m + 1
        
        return num[l]
            
            







