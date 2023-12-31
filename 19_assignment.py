# -*- coding: utf-8 -*-
"""19 assignment

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NBkRPYjrINy4knqdKo-saWsr1Tc-r3WD
"""

#1 solution

import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    # Create a min-heap
    min_heap = []


    for linked_list in lists:
        if linked_list:
            heapq.heappush(min_heap, (linked_list.val, linked_list))


    dummy = ListNode(0)
    current = dummy


    while min_heap:
        _, node = heapq.heappop(min_heap)
        current.next = node
        current = current.next
        if node.next:
            heapq.heappush(min_heap, (node.next.val, node.next))

    return dummy.next

#solution 2

def countSmaller(nums):
    def mergeSort(nums, start, end):
        if start == end:
            return [nums[start]], 0

        mid = (start + end) // 2
        left, left_count = mergeSort(nums, start, mid)
        right, right_count = mergeSort(nums, mid + 1, end)
        merged = []
        count = left_count + right_count

        left_ptr = 0
        right_ptr = 0
        while left_ptr < len(left) and right_ptr < len(right):
            if left[left_ptr] <= right[right_ptr]:
                merged.append(left[left_ptr])
                left_ptr += 1
            else:
                merged.append(right[right_ptr])
                right_ptr += 1
                count += len(left) - left_ptr

        merged.extend(left[left_ptr:])
        merged.extend(right[right_ptr:])
        return merged, count

    _, counts = mergeSort(nums, 0, len(nums) - 1)
    return counts

#3 solution

def sortArray(nums):
    def partition(nums, low, high):
        # Select the rightmost element as the pivot
        pivot = nums[high]
        i = low - 1

        for j in range(low, high):
            if nums[j] <= pivot:
                i += 1
                # Swap elements at indices i and j
                nums[i], nums[j] = nums[j], nums[i]

        # Swap the pivot with the element at index i+1
        nums[i + 1], nums[high] = nums[high], nums[i + 1]

        return i + 1

    def quicksort(nums, low, high):
        if low < high:
            # Partition the array and get the pivot index
            pivot_index = partition(nums, low, high)

            # Recursively sort the subarrays on both sides of the pivot
            quicksort(nums, low, pivot_index - 1)
            quicksort(nums, pivot_index + 1, high)

    # Call the quicksort function with the initial indices
    quicksort(nums, 0, len(nums) - 1)

    return nums

#4solution

def moveZeroes(nums):
    left = 0  # pointer for the non-zero elements
    right = 0  # pointer for iterating through the array

    while right < len(nums):
        if nums[right] != 0:
            # Swap non-zero element with the left pointer
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        right += 1

    return nums

#5 solution

def rearrangeArray(nums):
    length = len(nums)
    positive_idx = 0
    negative_idx = 0


    while positive_idx < length and nums[positive_idx] < 0:
        positive_idx += 1
    negative_idx = positive_idx


    while positive_idx < length and negative_idx < length:

        nums[positive_idx], nums[negative_idx] = nums[negative_idx], nums[positive_idx]
        positive_idx += 2
        negative_idx += 1

    return nums



