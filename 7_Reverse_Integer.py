class Solution(object):
    def reverse(self, x):
        if x >= 0:
            y = int(str(x)[::-1])
        else:
            y = -int(str(-x)[::-1])
        
        if y < -2**31 or y > 2**31 - 1:
            return 0 
        
        return y
