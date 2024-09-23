# import re

# mystr="this is python"

# x=re.match("this",mystr)

# if x:
#     print("match done")
# else:
#     print("error")    

import re

mystr="these is Python!215698"

x=re.findall('^Python',mystr)
#x=re.findall('^[A-Z]',mystr)
#x=re.findall('98$',mystr)

print(x)