class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        re=sorted(list(set(nums)))
        long=0
        it=0
        for i in range(len(re)-1):
            if re[i]+1 == re[i+1]:
                it+=1
            else:
                it=0
            long=max(long,it)
        return long+1
