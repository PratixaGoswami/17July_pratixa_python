''' Write a Python program to add 'ing' at the end of a given string (length
should be at least 3). If the given string already ends with 'ing' then add
'ly' instead if the string length of the given string is less than 3, leave it
unchanged.'''

str=input("Enter a string: ")

if len(str)>=3:
    if str.endswith('ing'):
        result=str.replace('ing','ly')
    else:
        result=str+'ing'
else:
    result=str

print("Modified string:",result)                