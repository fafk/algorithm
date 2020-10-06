"""
Recursively reverse a linked list and _return the new head_.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse(list: ListNode) -> ListNode:
    if not list.next:
        return list, list
    after, very_last = reverse(list.next)
    after.next = list
    list.next = None
    return list, very_last


