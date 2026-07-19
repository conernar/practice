def fast_sort(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[len(nums) // 2]
    left = [x for x in nums if x < pivot]
    middle = [x for x in nums if x == pivot]
    right = [x for x in nums if x > pivot]
    return fast_sort(left) + middle + fast_sort(right)


if __name__ == "__main__":
    print(fast_sort([4, 53, 13, 535, 31, 77, 13, 53, 55, 3675, 85, 34, 6, 2, 525, 24]))
