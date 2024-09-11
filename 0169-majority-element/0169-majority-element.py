class Solution(object):

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        dict_cout = {}
        for i  in nums:
            if i not in dict_cout:
                dict_cout.update({i: dict_cout.get(i, 0) + 1})
            else:
                dict_cout[i] += 1

        for i,j in dict_cout.items():
            if j > len(nums)/2:
                return i