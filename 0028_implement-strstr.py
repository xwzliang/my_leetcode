class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Time Limit Exceeded
        # Imagine two very long strings of equal lengths = n, haystack = “aaa…aa” and needle = “aaa…ab”
        # You should not do more than n character comparisons, or else your code will get Time Limit Exceeded

        # if not needle:
        #     return 0
        # for j in range(len(haystack)):
        #     i = 0
        #     k = j
        #     while i < len(needle) and k < len(haystack) and haystack[k] == needle[i]:
        #         k += 1
        #         i += 1
        #     if i == len(needle):
        #         return j
        # return -1

        for j in range(len(haystack) + 1):
            for i in range(len(needle) + 1):
                if i == len(needle):
                    return j
                if i + j == len(haystack):
                    return -1
                if needle[i] != haystack[i + j]:
                    break
