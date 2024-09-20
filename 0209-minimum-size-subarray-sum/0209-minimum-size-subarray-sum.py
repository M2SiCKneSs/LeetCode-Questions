class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        start_index = 0
        temp_count = 0
        min_count = float('inf')  # Initialize with a large number to represent infinity
        temp_sum = 0

        for i in range(len(nums)):
            temp_sum += nums[i]
            temp_count += 1

            # Check if current sum is greater than or equal to the target
            while temp_sum >= target:
                min_count = min(min_count, temp_count)  # Update the minimum count
                temp_sum -= nums[start_index]  # Shrink the window
                start_index += 1
                temp_count -= 1  # Decrease the count of elements in the window

        return min_count if min_count != float('inf') else 0  # Return 0 if no subarray found