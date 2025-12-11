letters = ['a', 'm', 'b', 'c', 'd', 'z', 'e', 'o', 'f', 'g']
print(letters)

# sort
letters.sort()
print(letters)

# sorted
# new_letters = sorted(letters) # lista nueva
# print(new_letters)

new_letters = letters[:]
# new_letters = letters.copy()
new_letters.sort()
print(new_letters)

# reverse
# new_letters = letters[::-1]
new_letters.reverse()
print(new_letters)
