class Solution:
    def isPalindrome(self, s: str) -> bool:
        store = ""

        for char in s:
            if char.isalnum():
                store += char.lower()

        return store == store[::-1]