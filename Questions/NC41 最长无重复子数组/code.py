#
# 
# @param arr int整型一维数组 the array
# @return int整型
#
class Solution:
    def maxLength(self , arr ):
        # write code here
        max_len=1
        res=list()
        for i in range(len(arr)):
            if arr[i] not in res:
                res.append(arr[i])
            else:
                res=res[res.index(arr[i])+1:]+[arr[i]]
            if len(res)>max_len:
                max_len=len(res)
        return max_len
      
# loop over the list, update the longest non-repeated sub-array and check the length at each step.
# !!! find the index of the repeated item and truncate the first part off.
