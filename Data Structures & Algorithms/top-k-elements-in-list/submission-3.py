class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        di=defaultdict(int)
        bu = [[] for _ in range(len(nums) + 1)]
        result=[]
        for i in nums:
            di[i] += 1
        for ke,i in di.items():
            bu[i].append(ke)

        
        for i in range(len(bu)-1,-1,-1):
            if bu[i]:
                result.extend(bu[i])
                
        return result[:k]
