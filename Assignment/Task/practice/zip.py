list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
list2 = [0, 1, 1, 0, 1, 2, 2, 0, 1]

sorted_list=[x for _,x in sorted(zip(list2,list1))]
print(sorted_list)
