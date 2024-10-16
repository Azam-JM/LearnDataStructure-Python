# Write a function that takes a string, s, as an input and determines whether or not it is a palindrome.
def is_palindrome(s):
    left = 0
  right = len(s) - 1
  while left < right:
    if s[left] != s[right]:
      return false
    left  = left + 1
    right = right - 1
  return true
