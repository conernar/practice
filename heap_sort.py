class heap:
    def sift_down(self, nums: list[int], n: int, i: int) -> list[int]:
        """
        堆排序下沉函数（Recursive method）:

        """
        # nums[4,10,3,5,1]
        idx_next_left = i * 2 + 1 #lift child idx
        idx_next_right = i * 2 + 2 # right child idx
        if  idx_next_left <= n - 1  and nums[i] < nums[idx_next_left]:
            nums[i], nums[idx_next_left] = nums[idx_next_left], nums[i]
            self.sift_down(nums, n, idx_next_left)
        if  idx_next_right <= n - 1 and nums[i] < nums[idx_next_right]:
            nums[i], nums[idx_next_right] = nums[idx_next_right], nums[i]
            self.sift_down(nums, n, idx_next_right)
        return nums

    def heap_sort(self, nums: list[int]) -> list[int]:
        n = len(nums)
        # build a MAX-HEAP
        for i in range(n // 2 - 1, -1, -1): # 最后一个非叶子节点idx = len // 2 - 1
            self.sift_down(nums, n, i)
        for i in range(n - 1):
            nums[0], nums[n - 1 - i] = nums[n - 1 -i], nums[0]
            self.sift_down(nums, n - 1 - i, 0)
        return nums

if __name__ == "__main__":
    nums = [4, 10, 3, 5, 1]
    nums1 = [4, 2 ,8, 7, 10, 9, 18, 3]
    h = heap()
    print(h.heap_sort(nums))
    print(h.heap_sort(nums1))




        
