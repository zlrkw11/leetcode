def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    
    mid = len(nums)//2
    l = merge_sort(nums[:mid])
    r = merge_srot(nums[mid:])
    return merge(l, r)

def merge(l, r):
    res=[]
    i = 0
    j = 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            res.append(l[i])
            i+=1
        else:
            res.append(r[j])
            j+=1

    while len(l):
        res.append(l[i])
        i += 1

    while len(r):
        res.append(r[j])
        j+=1
    return res

        

        