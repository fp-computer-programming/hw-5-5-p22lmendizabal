# author: LM (AMDG) 11/3/21
word =input("Enter a phrase: ")
if word == word[::-1]:
    print("The string " + word + " is a palindrome because the reverse is " + word[::-1])
else:
    print("The word " + word + " is not a palindrome because " + word + " spelled backwards is " + word[:: -1] + ".")