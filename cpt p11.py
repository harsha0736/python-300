def singleNumber(nums):
    single_number = 0
    for num in nums:
        single_number ^= num
    return single_number
  
nums=[1,2,1,2,6,7,6]
result=singleNumber(nums)
print(result)