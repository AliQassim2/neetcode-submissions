class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di={}
        for i in range(len(nums)):
            num=(target - nums[i])
            if  num in di:
                return [di[num],i]
            di[nums[i]]=i
        return []
