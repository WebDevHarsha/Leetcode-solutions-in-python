class Solution(object):
    def isPalindrome(self, x):
        x=str(x)
        if x[0]=="-":
            return False
        elif x[::-1]==x:
            return True
        else:
            return False