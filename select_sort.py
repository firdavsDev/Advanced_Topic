nums = [8,5,6,7,4,2,3]

def select(nums, start):
    n = len(nums)
    pos = start
    for i in range(pos, n):
        if nums[i] < nums[pos]:
            pos = i
    return pos

# print(select(nums, 0))
  
def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        pos = select(nums, i)
        nums[pos], nums[i] = nums[i], nums[pos]
    print(nums)
        
selection_sort(nums)
