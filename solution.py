from typing import List


class Solution:
    # QUESTION: https://leetcode.com/problems/two-sum/
    def twoSum(self, nums: List[int], target:int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

    #QUESTION: https://leetcode.com/problems/palindrome-number/
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

    #Question: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
    def removeDuplicates(self, nums: List[int]) -> int:
        for ele in nums:
            while nums.count(ele) > 1:
                nums.remove(ele)
        return len(nums)
