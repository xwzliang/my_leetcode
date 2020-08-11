class Solution:
    def reverseWords(self, s: str) -> str:
        words = [x for x in s.split(" ") if x]
        return " ".join(words[::-1])
