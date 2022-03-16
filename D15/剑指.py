# 剑指 Offer 03. 数组中重复的数字
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] =1
            else:
                dic[num] = dic[num] +1
                res =num
        return res

# 剑指 Offer 53 - I. 在排序数组中查找数字
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        i = 0
        res = 0
        Done = False
        while(i<n) and  not Done:
            if nums[i]<target:
                i = i +1
            elif nums[i] == target:
                res = res +1
                i = i +1
            elif nums[i]>target:
                Done =True
        return res

# 剑指 Offer 53 - II. 0～n-1中缺失的数字
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len (nums)
        end = False
        for i in range(n):
            if i == nums[i]:
                i = i +1
            else:
                res = i
                end = True
                break
        if not end:
            res = n
        return res

list = [2,5,7,3,45,2,3,6]
print(Solution.findRepeatNumber(list))