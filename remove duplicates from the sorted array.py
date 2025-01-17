nums = [1,1,2,2,3,4,5,5,6]

def removeDuplicates(nums):
  if not nums:
      return 0
  
  i = 0 #slow pointer

  for j in range(1, len(nums)):
      if nums[j] != nums[i]:
          i += 1
          nums[i] = nums[j]
        
  return i + 1

result = removeDuplicates(nums)
print("updated array:", nums[:result])

