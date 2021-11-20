def kbig(nums, k):
    for ankarats in range(len(nums) - 1):
        for lafnat in range(len(nums) - ankarats, len(nums) - 1):
            if nums[lafnat] > nums[lafnat + 1]:
                nums[lafnat], nums[lafnat + 1] = nums[lafnat + 1], nums[lafnat]
    return nums[-k]
