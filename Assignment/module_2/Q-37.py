""" Write a Python program to check multiple keys exists in a dictionary"""
my_dict={'name':'pratixa',
            'subject':'python',
             'age':24,
             'education':'BE'}
             
key_to_check=['age','subject','education','hobbies']

all_keys_exist= all(i in my_dict for i in key_to_check)
if all_keys_exist:
        print("All keys exist in the dictionary.")
else:
        print("Some keys are missing in the dictionary.")
  


