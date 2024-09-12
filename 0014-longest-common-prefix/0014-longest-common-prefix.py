class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        first_word = strs[0]
        index = 1

        # Continue until the prefix matches in all words
        while index <= len(first_word):
            # Extract the current prefix
            current_prefix = first_word[:index]

            # Check if this prefix is the same in all other words
            for word in strs[1:]:
                if not word.startswith(current_prefix):  # If any word doesn't match, return the prefix so far
                    return first_word[:index - 1]
            index += 1
        return first_word