class Solution(object):
    def removeDuplicates(self, nums):
        # Initialize index for the position where we will place valid elements
        index = 0

        for i in range(len(nums)):
            # If it's the first occurrence of the element or the second occurrence, copy it
            if index < 2 or nums[i] != nums[index - 2]:
                nums[index] = nums[i]
                index += 1

        # Return the updated length and the modified array
        return  index  # nums[:index] is the final result with only k elements