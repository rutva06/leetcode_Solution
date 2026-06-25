from collections import defaultdict
from typing import List

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def atMost(k):
            left = 0
            count = 0
            freq = defaultdict(int)

            for right in range(len(nums)):
                freq[nums[right]] += 1

                while len(freq) > k:
                    freq[nums[left]] -= 1

                    if freq[nums[left]] == 0:
                        del freq[nums[left]]

                    left += 1

                count += (right - left + 1)

            return count

        return atMost(k) - atMost(k - 1)