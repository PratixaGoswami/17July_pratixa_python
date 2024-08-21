"""Write a Python script to sort (ascending and descending) a dictionary by
value."""

student={'name':'pratixa','subject':'python'}

sorted_asc = dict(sorted(student.items()))
print("Dictionary sorted by value (ascending):")
print(sorted_asc)

sorted_desc = dict(sorted(student.items(),reverse=True))
print("Dictionary sorted by value (descending):")
print(sorted_desc)

