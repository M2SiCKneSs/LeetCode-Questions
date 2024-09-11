class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        
        This function rotates the list `nums` to the right by `k` steps.
        The rotation is done by slicing the array and rearranging its elements.
        """

        # Ensure k is within the bounds of the array length. 
        # If k is greater than the length of nums, rotating more than the length is the same as k % len(nums).
        k = k % len(nums)      

        # Calculate the point where we will split the list (from the back).
        # This is the length of nums minus the number of rotations.
        r = len(nums) - k

        # Create a new list containing the first part of the array (elements before index r).
        new = nums[0:r]  

        # Remove the first part (up to index r) from the original array (in-place modification).
        nums[0:r] = []  

        # Extend the remaining part of the array (already rotated) by adding the removed part (new).
        nums.extend(new)
