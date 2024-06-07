class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # create a map
        # update the frequency
        # iterate the second string
        # reduce the freq from map1 if present
        # if not present -> False
        # Once done
        # check if all map key are zero
        # yes -> True
        # else - False
        hashMap = {}

        for val in range(len(s)):
            if s[val] in hashMap:
                hashMap[s[val]] += 1
            else:
                hashMap[s[val]] = 1
        
        # Run through t
        for word in range(len(t)):
            if t[word] not in hashMap or hashMap[t[word]] < 0:
                return False
            else:
                hashMap[t[word]] -= 1
        
        # Check if valid
        for value in hashMap.keys():
            if hashMap[value] != 0:
                return False
        
        return True
