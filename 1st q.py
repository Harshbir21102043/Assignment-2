str1 = "Python is a case sensitive language"
print(len(str1))

# b. Reverse the order of the string in one line code.
str1 = "Python is a case sensitive language"
print(str1[::-1])

# c. Using Slice function store “a case sensitive” in new string.
str1 = "Python is a case sensitive language"
str2 = str1[10:26]
print(str2)

# d. Replace “a case sensitive” with “object oriented”.
str1 = "Python is a case sensitive language"
print(str1.replace("a case sensitive", "object oriented"))

# e. Find index of substring “a” in the given input string.
str1 = "Python is a case sensitive language"
print(str1.find("a"))

# f. Remove the white spaces from the given input string.
str1 = "Python is a case sensitive language"
#to replace white spaces we can replace spaces with blank
print(str1.replace(" ", ""))
