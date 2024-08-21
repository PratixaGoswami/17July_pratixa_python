import os
if os.path.exists("test.txt"):
    os.remove('test.txt')
    print("the file is file sucessfully deleted")
else:
    print("the file does not exit ")    