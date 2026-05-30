class Solution:
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



if __name__ == "__main__":
    input1, k = [1,2,2,3,3,3], 2
    input2, k2 = [7,7], 1
    sol = Solution()
    print(sol.topKFrequent(input1, k))
    print(sol.topKFrequent(input2, k2))
