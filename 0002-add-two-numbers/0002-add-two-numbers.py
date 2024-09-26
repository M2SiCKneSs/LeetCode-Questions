class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_new=[]
        l2_new=[]
        
        while l1:
            l1_new.append(l1.val)
            l1=l1.next

        while l2:
            l2_new.append(l2.val)
            l2=l2.next
        l1_new.reverse()
        l2_new.reverse()
        num1 = int(''.join(map(str, l1_new)))
        num2 = int(''.join(map(str, l2_new)))
        #print(num1,num2)

        # Sum the two numbers
        total = num1 + num2

        # Convert the sum back to a string and then to a linked list
        total_str = str(total)
        total_str=total_str[::-1]
        sum1 = ListNode(int(total_str[0]))  # Initialize with the first digit
        current = sum1

        # Create the rest of the nodes
        for i in total_str[1:]:
            current.next = ListNode(int(i))  # Add the next digit as a new node
            current = current.next  # Move to the next node

        # Print the resulting linked list
        return sum1