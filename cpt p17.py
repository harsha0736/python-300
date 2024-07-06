def maximum_index(nums):
    distinct_nums=set(nums)
    sorted_list=sorted(distinct_nums,reverse=True)
    for i in range(len(nums)):
        return sorted_list[2]
    else:
        return sorted_list[0]


nums = [16,36,58 ]
result=maximum_index(nums) 
print(result)          
