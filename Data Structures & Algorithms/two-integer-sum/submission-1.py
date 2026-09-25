class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di={}
        for i in range(len(nums)):
            cur=nums[i]
            num=(target - cur)
            if  num in di:
                return [di[num],i]
            di[cur]=i
        return []
