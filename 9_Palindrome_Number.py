class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_str = str(x)
        x_reverse_str = x_str[::-1]
        if(x_str == x_reverse_str):
            return True
        else:
            return False
        
