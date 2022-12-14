from audioop import reverse
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

    #QUESTION: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
    def removeDuplicates(self, nums: List[int]) -> int:
        for ele in nums:
            while nums.count(ele) > 1:
                nums.remove(ele)
        return len(nums)

    #QUESTION: https://leetcode.com/problems/crawler-log-folder
    def minOperations(self, logs: List[str]) -> int:
        i = 0
        for command in logs:
            if command == "./":
                pass
            elif command == "../":
                i = i - 1
                if i < 0:
                    i = 0
            else:
                i = i + 1
        if i < 0:
            return 0
        else:
            return i


# Below: SUDA

def func1(n:int) -> int:
    res = 0
    for i in range(0,n+1):
       if not (i % 9 == 0 or '9' in str(i).split()):
           res = res + i * i
    return res

def func2(lst: List) -> int:
    if len(lst) == 0:
        return 0
    count = {}
    for nums in lst:
        count[nums] =  count.get(nums, 0) + 1
    count = sorted(count, key=count.get, reverse=True)
    return count[0]

print(func2([3,5,5,3,5,9]))



