class Solution:
    def maxArea(self, h: List[int]) -> int:
        maxarea=0
        l=0
        r=len(h)-1
        while(l <= r):
            cal=self.calArea(h,l,r)
            maxarea =  cal if maxarea < cal else maxarea
            if h[l] > h[r]:
                r-=1
            else:
                l+=1
        return maxarea
            
    def calArea(self,h:List[int],l:int,r:int)->int:
        height=min(h[l],h[r])
        width=r-l
        return height*width