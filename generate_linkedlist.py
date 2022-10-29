from typing import List

class ListNode:
    def __init__(self, value=0, next=None) -> None:
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, nums: List) -> None:
        self.nums = nums
        self.head = ListNode(nums[0], nums[1])
        current = self.head
        for i in range(1, len(nums)):
            if i + 1 == len(nums):
                current.next = ListNode(nums[i], None)
            else:
                current.next = ListNode(nums[i], nums[i + 1])
            current = current.next

    def linkedList_array(self) -> List:
        result = []
        current = self.head
        while current:
            result.append(current)
            current = current.next
        return result
    
    def print_linkedList(self) -> None:
        for node in self.linkedlist_array:
            print(node.value)
            if not node.next:
                print(node.next)
            else:
                print(node.next.value)
            print("############")

