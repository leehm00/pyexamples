from typing import Literal


class Solution:
    def decide(self,str:Literal)->bool:
        lcount =0
        rcount =0
        l = 0
        r = 0
        n = len(str)
        for i in range(int(n/2)):
            if str[i] == '?':
                lcount+=1
            else:
                l += int(str[i])
        for i in range(int(n/2),n):
            if str[i] == '?':
                rcount+=1
            else:
                r += int(str[i])
        #print(lcount,rcount)
        #特殊情况
        if lcount+rcount == 0:
            if not l == r:
                return True
            else:
                return False
        #print(l,r)
        if (lcount + rcount )%2==0:
            if (l-r) == 9/2*(rcount-lcount):
                return False
            else:
                return True
        else:
            return True

        


solu = Solution
print(solu.decide(self = solu,str="25??"))
print(solu.decide(self = solu,str="?3295???"))
print(solu.decide(self = solu,str="5023"))