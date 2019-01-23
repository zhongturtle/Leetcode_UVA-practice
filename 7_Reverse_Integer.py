class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        lowest_bound = -1 * 2**31
        highest_bound = 2**31 -1
        num = str(x)
        if (num[0] == '-'):
            minus = True
            m = num[::-1]
            l = m[:len(m)-1]
            # print(l)
        else:
            minus = False
            num = num[::-1]
        if(minus):
            h = '-' + l
            if (int(h) < lowest_bound):
                return 0
            return int(h)
        if (int (num) > highest_bound):
                return 0
        return int(num)