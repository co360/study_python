def cal(p1, p2, *nums):
    print nums
    sum = p1**2 + p2**2
    for num in nums:
        sum += num**2
    return sum

print cal(1,2, 4,5)

def cal1(p1,p2,**args):
    print args

cal1(1,2,name='wmsj',age=12)