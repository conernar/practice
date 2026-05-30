class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        sorted_str_dict = {}
        for i, s in enumerate(strs):
            temp_str = "".join(sorted(s))
            if temp_str in sorted_str_dict:
                sorted_str_dict[temp_str].append(s)
            else:
                sorted_str_dict[temp_str] = [s]
        res_lst = []
        for v in sorted_str_dict.values():
            res_lst.append(v)
        return res_lst

class SolutionO:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # use collections.defaultdict to create [] defaultly when insert
        from collections import defaultdict
        sorted_str_dict = defaultdict(list)
        for s in strs:
            sorted_str_dict["".join(sorted(s))] = s
        
        # .values returns a literable object so just use list() to convert!
        return list(sorted_str_dict.values())



if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1
    test1 = ["act", "pots", "tops", "cat", "stop", "hat"]
    # Expected: [["hat"], ["act", "cat"], ["pots", "tops", "stop"]] (in any order)
    print("Test 1:", sol.groupAnagrams(test1))
    
    # Test Case 2
    test2 = ["x"]
    # Expected: [["x"]]
    print("Test 2:", sol.groupAnagrams(test2))
    
    # Test Case 3
    test3 = [""]
    # Expected: [[""]]
    print("Test 3:", sol.groupAnagrams(test3))

