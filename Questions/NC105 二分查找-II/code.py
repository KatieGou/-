class Solution:
    def search(self , nums , target ):
#         if target in nums:
#             return nums.index(target)
#         return -1
#         write code here
        i, j=0, len(nums)-1
        while i<=j:
            m=(i+j)//2
            if nums[m]==target:
                idx=m
                while idx>=0 and nums[idx]==target:
                    idx-=1
                return idx+1
            elif nums[m]>target:
                j=m-1
            else:
                i=m+1
        return -1
      
# 1. while i<=j, not i<j
# 2. j should be len(nums)-1, not len(nums), to avoid empty list cases
# 3. if the target is not found, j=m-1 or i=m+1, not j=m or i=1, to reduce running time
