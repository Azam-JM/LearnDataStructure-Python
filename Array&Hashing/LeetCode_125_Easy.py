class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = ""
        for word in range(len(s)):
            if s[word].isalpha():
                newString += s[word].lower()
            elif s[word].isdigit():
                newString += s[word]
        
        # Traverse it with 2 pointers
        leftPointer = 0
        rightPointer = len(newString) - 1
        while leftPointer <= rightPointer:
            if newString[leftPointer] != newString[rightPointer]:
                return False
            else:
                leftPointer += 1
                rightPointer -= 1
        
        return True
        
