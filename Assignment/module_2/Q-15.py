""" Write a Python program to get unique values from a list"""
def unique_list(input_list):
    
    input_list=[]
    new_list=set(input_list)
    return new_list
  


 
original_list=[1,2,2,3,4,5,6,5,6,5,]  
result=set(original_list)
print("original list:",original_list)
print("list with unique element:",result)
