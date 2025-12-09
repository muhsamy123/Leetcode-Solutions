# LeetCode Problem: 1122. Relative Sort Array
https://leetcode.com/problems/relative-sort-array/


from collections import Counter
from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = Counter(arr1)
        result = []
        
        # Add elements in the order of arr2
        for num in arr2:
            result.extend([num] * freq[num])
            freq.pop(num)
        
        # Add remaining elements sorted
        remaining = []
        for key, value in freq.items():
            remaining.extend([key] * value)
        remaining.sort()

        result.extend(remaining)
        return result


