from typing import List


class Solution:#动态规划
    def decide(self,nums:List[List[int]])->int:
        m = len(nums)
        n = len(nums[0])
        f = n*[0]
        for i in range(m):
            temp = n*[0]
            maxf = -1000000000
            for j in range(n):#正序
                maxf = max(maxf,f[j]+j)
                #print("max",maxf)
                temp[j]=max(temp[j],maxf+nums[i][j]-j)
            #print(temp)
            maxf2 = -1000000000
            for j in range(n-1,-1,-1):#倒序
                maxf2 = max(maxf2,f[j]-j)
                #print("max",maxf)
                temp[j]=max(temp[j],maxf2+nums[i][j]+j)
            #print(temp)
            f = temp
        #print(max(temp))
        return max(f)

solu = Solution
print(solu.decide(self = solu,nums=[[1,5],[2,3],[4,2]]))
print(solu.decide(self = solu,nums=[[1,2,3],[1,5,1],[3,1,1]]))
