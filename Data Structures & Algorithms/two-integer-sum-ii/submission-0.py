class Solution:
    def twoSum(self, n: List[int], t: int) -> List[int]:
        if not n:
            return -1
        l=0
        r=len(n)-1
        while (l<r):
            if(n[l]+n[r] > t):
                r-=1
            elif(n[l]+n[r] < t):
                l+=1
            else:
                return [l+1,r+1]