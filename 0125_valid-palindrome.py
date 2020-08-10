# import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # str_alphanumeric = "".join(re.findall("[a-z0-9]+", s.lower()))
        # head = 0
        # tail = len(str_alphanumeric) - 1
        # for i in range(int(len(str_alphanumeric) / 2)):
        #     if str_alphanumeric[head] != str_alphanumeric[tail]:
        #         return False
        #     head += 1
        #     tail -= 1
        # return True

        head = 0
        tail = len(s) - 1
        while head < tail:
            while head < tail and not s[head].isalnum():
                head += 1
            while head < tail and not s[tail].isalnum():
                tail -= 1
            if s[head].lower() != s[tail].lower():
                return False
            head += 1
            tail -= 1
        return True
