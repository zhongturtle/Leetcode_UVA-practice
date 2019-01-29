class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        left_part = ['(', '{', '[']
        right_part = [')', '}',']']
        if len(s) == 0:
            return True
        elif len(s) == 1:
            return False
        for i in s:
            if i in left_part:
                stack.append(i)
            if i in right_part:
                if len(stack) == 0:
                    return False
                else:
                    if right_part.index(i) == left_part.index(stack[-1]):
                        stack.pop()
                    else:
                        return False
                
        if len(stack) != 0:
            return False
        else:
            return True
                
