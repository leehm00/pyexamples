from typing import List


class Solution:
    def decide(self,nums:List)->int:

        n = len(nums)
        jishu = 0
        oushu = nums[0]
        for i in range(n):
            jishu = max(oushu-nums[i],jishu)
            oushu = max(jishu+nums[i],oushu)
            #print(oushu,jishu)
        return oushu


solu = Solution
print(solu.decide(self = solu,nums=[5,6,7,8]))
print(solu.decide(self = solu,nums=[4,2,5,3]))
print(solu.decide(self = solu,nums=[6,2,1,2,4,5]))