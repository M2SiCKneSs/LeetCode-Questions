class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_map = {}  # Dictionary to store the last index of each character
        max_length = 0
        start = 0  # Start of the current substring
        i = 0  # Manual index counter

        for char in s:
            if char in char_map and char_map[char] >= start:
                # Move the start to the right of the previous index of the repeated character
                start = char_map[char] + 1

            # Update the last index of the character
            char_map[char] = i

            # Calculate the current length and update max_length
            max_length = max(max_length, i - start + 1)
            
            i += 1  # Manually increment the index

        return max_length