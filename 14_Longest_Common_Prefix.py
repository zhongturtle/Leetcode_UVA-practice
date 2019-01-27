class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        i=0
        list_len=len(strs)
        lcp=''
        if list_len == 1:
            return strs[0]
        while True:
            try:
                pre_word = strs[0][i]
            except:
                return lcp
            for index in range(1, list_len):
                try:
                    cur_word = strs[index][i]
                    
                    if pre_word == cur_word:
                        if index == list_len - 1:
                            lcp = lcp + pre_word
                            i = i + 1
                        else:
                            pre_word = cur_word
                    else:
                        return lcp
                except:
                    return lcp
