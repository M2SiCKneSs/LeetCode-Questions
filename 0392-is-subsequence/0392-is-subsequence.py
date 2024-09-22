class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        start,end = 0,0
        while start<len(s) and end<len(t):
            if s[start] == t[end]:
                start += 1
                end += 1
            else:
                end +=1
        if start==len(s):
            return True
        else:
            return False