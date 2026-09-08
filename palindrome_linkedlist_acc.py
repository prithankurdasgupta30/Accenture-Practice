class ListNode:
        def __init__(self, val=0, next=None):
                self.val = val
                self.next = next
def isPalindrome(head):
        values = []
        current = head
        while current:
                values.append(current.val)
                current = current.next
        return values == values[::-1]
values = list(map(int, input().split()))
head = ListNode(values[0])
current = head
for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
print(isPalindrome(head))