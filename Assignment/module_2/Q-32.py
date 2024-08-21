"""Write a Python script to concatenate following dictionaries to create a
new one."""

data={'name':'pratixa','subject':'python'}
data2={'age':24}
new_data={}
new_data.update(data)
new_data.update(data2)
print(new_data)