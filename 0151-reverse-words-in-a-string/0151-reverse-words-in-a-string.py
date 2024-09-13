
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        list_2_str=""
        str_list=s.split(" ")
        for i in range(len(str_list)//2):
            temp=str_list[i]
            str_list[i]=str_list[-i-1]
            str_list[-i-1]=temp
        def remove_spaces(s):
            if s == " ":
                return ""
            else:
                return s
        list_2_str = ' '.join(filter(remove_spaces,str_list))
        return list_2_str