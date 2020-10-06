"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

    Only constant extra memory is allowed.
    You may not alter the values in the list's nodes, only nodes itself may be changed.

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseKGroup(node: ListNode, k: int):
    def rec(node: ListNode, k: int, depth=1):
        if not node.next:
            return node, node, None, depth

        after, current_chain_last, prev_chain_last, length = rec(node.next, k, depth + 1)
        if depth > (length - (length % k)):
            return node, node, node, length
        else:
            if depth % k == 0:
                return node, node, current_chain_last, length
            if depth % k == 1:
                after.next = node
                node.next = prev_chain_last
                return node, current_chain_last, prev_chain_last, length
            else:
                after.next = node
                return node, current_chain_last, prev_chain_last, length

    return rec(node, k)[1]
