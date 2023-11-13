
class Solution:
    def decide(self,num:int)->int:
        if not num%2==0:
            return (pow(5,int(num/2)+1)*pow(4,int(num/2)))%(pow(10,9)+7)
        else:
            return (pow(5,int(num/2))*pow(4,int(num/2)))%(pow(10,9)+7)

solu = Solution
print(solu.decide(self = solu,num=4))
