class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        di=set()
        for i in nums:
            if i in di:
                return True
            di.add(i)
        return False