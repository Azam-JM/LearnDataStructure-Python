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
# Sample2 
class Solution:
    def checkIfAlpha(self, s: str) -> bool:
        if ('a' <= s <= 'z') or ('A' <= s <= 'Z'):
            return True
        return False
    
    def checkIfDigit(self, s: str) -> bool:
        if '0' <= s <= '9':
            return True
        return False

    def isPalindrome(self, s: str) -> bool:
        newString = ""
        for word in range(len(s)):
            if self.checkIfAlpha(s[word]):
                newString += s[word].lower()
            elif self.checkIfDigit(s[word]):
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
        
        
