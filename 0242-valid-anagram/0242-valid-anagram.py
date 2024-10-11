class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        newdict={'a': 0, 'c': 0, 'b': 0, 'e': 0, 'd': 0, 'g': 0, 'f': 0, 'i': 0,'h': 0, 'k': 0,
                 'j': 0, 'm': 0, 'l': 0, 'o': 0, 'n': 0, 'q': 0, 'p': 0, 's': 0,'r': 0, 'u': 0, 
                 't': 0, 'w': 0, 'v': 0, 'y': 0, 'x': 0, 'z': 0}
        for i in s:
            newdict[i] += 1
        for i in t:
            newdict[i] -= 1
        for i in newdict:
            if newdict[i] != 0:
                return False
        return True
            
            