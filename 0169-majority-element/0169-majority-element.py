class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        This function returns the majority element, which appears more than len(nums)/2 times in the list.
        """
        
        # Initialize an empty dictionary to count occurrences of each element
        dict_count = {}
        
        # Iterate through the list and count occurrences of each element
        for i in nums:
            if i not in dict_count:  # If the element is not in the dictionary
                # Add it to the dictionary with a count of 1 (using .get(i, 0) to ensure count starts at 0)
                dict_count.update({i: dict_count.get(i, 0) + 1})
            else:
                # If the element is already in the dictionary, increment its count by 1
                dict_count[i] += 1

        # Iterate through the dictionary to find the majority element
        for element, count in dict_count.items():
            # If an element's count is greater than half the length of the list, return it as the majority element
            if count > len(nums) / 2:
                return element
