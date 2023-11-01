
# Strings and Lists

#  creating a list from strings

a = 'bangladesh is my country'

b = list(a)

print(b)

# split(): for separeting each word in the list not a single letter

a = 'bangladesh is my country'

b = a.split()

print(b)

# spliting using special symbol

a = 'bangladesh-is-country'
delimiter = '-'
b = a.split(delimiter) # mentioning '-' is a separator
# we can also use 'space' to separate the strings
print(b)


# List to string

print(delimiter.join(b))