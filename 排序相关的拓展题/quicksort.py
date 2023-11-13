import random

def qsort(nums,begin,end):
    if begin>=end:
        return 
    target = nums[begin]
    l =begin
    r = end
    while l<r:
        while l<r and nums[r]>target:# 从右向左找，直到找到一个小于等于target的位置
            r-=1
        nums[l]=nums[r]# 把这个值赋值给最左边的位置
        while l<r and nums[l]<=target:# 然后从左往右找，直到找到一个大于target的位置
            l+=1
        nums[r]=nums[l]# 把这个值赋值给最右边的位置 
    nums[l]=target # 最后跳出循环的条件是l==r，这就是target需要插入的位置
    qsort(nums,begin,l-1)# 递归左半边
    qsort(nums,l+1,end)# 递归右半边

nums = [random.randint(1,20)for _ in range(10)]
print(nums)
qsort(nums,0,len(nums)-1)
print(nums)