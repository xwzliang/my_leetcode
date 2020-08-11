class Solution:
    def reverse(self, x: int) -> int:
        reversed_int = 0
        sign = 1
        if x < 0:
            sign = -1
            x = abs(x)
        while x:
            # 214748364 = 2 ** 31 / 10
            if reversed_int > 214748364:
                return 0
            reversed_int = reversed_int * 10 + x % 10
            x //= 10
        # return_int = reversed_int * sign
        # if return_int < -(2 ** 31) or return_int > 2 ** 31 - 1:
        #     return 0
        # return return_int
        return reversed_int * sign


# if __name__ == "__main__":
#     print(Solution().reverse(-123))
