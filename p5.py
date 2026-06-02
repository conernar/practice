class Solution1:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        from collections import defaultdict
        int_dic = defaultdict(int)
        for num in nums:
            int_dic[num] = int_dic.get(num, 0) + 1
        res = [0] * k
        for i in range(k):
            
            fre_max = 0
            for key in int_dic:
                if int_dic[key] > fre_max and (i == 0 or key not in res[:i]):
                    fre_max = int_dic[key]
                    res[i] = key
        return res
class Solution2:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # use Counter to solve easily.
        from collections import Counter
        d = Counter(nums)
        res = []
        for i in d.most_common(k):
            res.append(i[0])
        return res

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        # use original heapq in python is also elegant
        import heapq
        # heapify returns None and it changes a list directly.
        heap = []
        for key, v in d.items():
            heapq.heappush(heap, (-v, key))
        
        res = []
        for _ in range(k):
            neg_freq, num = heapq.heappop(heap)
            res.append(num)
        return res
        



if __name__ == "__main__":
    input1, k = [1,2,2,3,3,3], 2
    input2, k2 = [7,7], 1
    sol = Solution()
    print(sol.topKFrequent(input1, k))
    print(sol.topKFrequent(input2, k2))
