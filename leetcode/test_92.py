import unittest
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseBetween(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    # reverse nodes from position left to position right.
    # Brute-forth
    if left == right or head.next is None:
        return head
    # Make an array that has size is equal to nodes
    array = []
    # Copy array from Linked List
    while head is not None:
        array.append(head)
        prev = head
        head = head.next

    # reverse the nodes form left position to right position
    gap = right - left
    right_node = array[(right - 1)]
    for i in range(1, gap + 1):
        # Prevent Circle Linked-List error
        right_node.next = None
        array[(right - 1) - i].next = None
        right_node.next = array[(right - 1) - i]
        right_node = array[(right - 1) - i]

    if left != 1:
        array[left - 2].next = array[right - 1]
    if right != len(array):
        array[left - 1].next = array[right]

    # The head of node must be changed
    if left == 1:
        return array[right - 1]
    return array[0]


def test_1():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    left = 2
    right = 4
    expected = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5)))))
    assert reverseBetween(head, left, right).val == expected.val
    assert True
