class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapping = {}
        for i in range(len(s)):
            if s[i] in mapping and mapping[s[i]] == t[i]:
                continue
            elif s[i] not in mapping:
                if t[i] in mapping.values():
                    return False
                mapping[s[i]] = t[i]
            else:
                return False
        return True