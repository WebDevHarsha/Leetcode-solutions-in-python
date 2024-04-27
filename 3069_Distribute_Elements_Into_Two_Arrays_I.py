class Solution(object):
    def resultArray(self, nums):
        arr1=[nums[0]]
        arr2=[nums[1]]
        l=len(nums)
        for i in range(2,l):
            if arr1[-1]>arr2[-1]:
                arr1.append(nums[i])
            elif arr1[-1]<arr2[-1]:
                arr2.append(nums[i])
        return arr1+arr2
