def rotate_array(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    nums = nums[k:] + nums[:k]
    print(nums)


rotate_array([1,2], 1)