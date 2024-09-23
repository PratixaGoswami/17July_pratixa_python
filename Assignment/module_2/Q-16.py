"""Write a Python program to check whether a list contains a sub list"""
original_list=[1,2,3,4,5,6]
sub_list=[2,3,4,5] 

if str(sub_list)[1:-1] in str(original_list)[1:-1]:
    print("list contain a sub list")
else:
    print("list not contain a sub list")    
  