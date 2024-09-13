
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        str_list=s.split(" ")

        "Reverse the list of words in place by swapping elements"
        for i in range(len(str_list)//2):
            temp=str_list[i]
            str_list[i]=str_list[-i-1]
            str_list[-i-1]=temp

        "Use the lambda function to filter out spaces"
        remove_spaces = lambda s: "" if s == " " else s
        list_2_str = ' '.join(filter(remove_spaces,str_list))
        return list_2_str