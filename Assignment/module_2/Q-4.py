""" Write a Python function to get the largest number, smallest num and sum
of all from a list."""

def list(num):

    largest=max(num)
    smalest=min(num)
    total_sum=sum(num) 

    return largest,smalest,total_sum

num=[1,2,3,4,5,6,7,8]

largest,smalest,total_sum= list(num)
print(num)
print("largest:",largest)
print("Smalest:",smalest)
print("total sum :",total_sum)




  


