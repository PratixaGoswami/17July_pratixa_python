"""Write a Python function that takes two lists and returns true if they have
at least one common member."""

list1=["Hello","Hi","pinal"]
list2=["Noon","Evening","Hi"]
common_member=False
for i in list1:
    if i in list2:
        common_member=True
        break
print(common_member)



