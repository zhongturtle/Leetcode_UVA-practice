class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        value_table = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        sum = 0
        for i, item in enumerate(s):
                if i != len(s) - 1 and value_table.get(item) < value_table.get(s[i+1]):
                    sum -= value_table.get(item)
                else:
                    sum += value_table.get(item)
                
        return sum
