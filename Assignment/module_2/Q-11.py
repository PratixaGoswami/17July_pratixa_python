"""Write a Python function that takes a list and returns a new list with unique
elements of the first list."""
def unique_list(input_list):
    
    input_list=[]
    new_list=set(input_list)
    return new_list
  

        

 
original_list=[1,2,2,3,4,5,6,5,6,5,]  
result=set(original_list)
print("original list:",original_list)
print("list with unique element:",result)