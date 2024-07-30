''' Write a Python program to find the first appearance of the substring
'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the
whole 'not'...'poor' substring with 'good'. Return the resulting string.'''

str= input("Enter a string: ")

not_word = str.find('not')
poor_word = str.find('poor')

if not_word != -1 and poor_word!= -1:
  
    if not_word < poor_word:
        
        result=str[:not_word] + 'good' + str[poor_word + 4:]
        print(result)  
else:
    print(str)