# 方法1:从后往前遍历，遇相同删除当前项
def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    for num in range(len(nums)-1, 0, -1):
        if nums[num] == nums[num-1]:
            nums.pop(num)
    return len(nums)


# 方法2:只是为了计数，不删除
def removeDuplicates2(nums):
    index = 1
    for i in range(len(nums)-1):
        if(nums[i] != nums[i+1]):
            nums[index] = nums[i+1]
            index += 1
    return(index)


# 方法3:双指针
def removeDuplicates3(self, nums):
    if not nums:
        return 0
    slow = fast = 0
    while fast <= len(nums) - 1:
        if nums[fast] != nums[slow]:
            nums[slow+1] = nums[fast]
            slow += 1
        fast += 1
    return slow + 1
