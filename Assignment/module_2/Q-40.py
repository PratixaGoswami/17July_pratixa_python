""" Write a Python program to combine two dictionary adding values for
common keys.
d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,'d':400}
"""
d1 = {'a': 100, 'b': 200, 'c':300} 
d2 = {'a': 300, 'b': 200,'d':400}
emty_d={}
for i in d1:
    emty_d[i]=d1[i]
for i in d2:
    if i in emty_d:
        emty_d[i]+=d2[i]
    else:
        emty_d[i]=d2[i]        

     
print(emty_d)     