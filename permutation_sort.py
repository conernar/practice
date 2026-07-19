from itertools import permutations


def permutation_sort(nums):

    for lst in permutations(nums):
        if all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1)):
            return lst


if __name__ == "__main__":
    print(permutation_sort([4, 24, 3, 41, 41, 3, 34, 15, 77, 57]))
