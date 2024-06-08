class Solution(object):
    def removeElement(self, nums, val):
        l=nums.count(val)
        for i in range (l):
            nums.remove(val)
        return len(nums)
