 #Palindrom Fundamental exercise

s = input("Give me a word or phrase and let's see if it's a Palindrome!")

def palindrome(s):
  i = 0
  j = len(s) -1
  while i < j:
    while not s[i].isalnum() and i < j:
      i += 1
    while not s[j].isalnum() and i <j:
      j -= 1  
    if s[i].lower() != s[j].lower():
      return False
    i += 1
    j -= 1
  return True

print(palindrome(s))