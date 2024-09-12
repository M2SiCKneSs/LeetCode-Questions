class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0

        num_of_jumps = 0
        max_reachable = 0  
        current_end = 0  

        for i in range(len(nums) - 1):
            max_reachable = max(max_reachable, i + nums[i])

            if i == current_end:
                num_of_jumps += 1
                current_end = max_reachable

                if current_end >= len(nums) - 1:
                    break

        return num_of_jumps