#  Write python program that user to enter only odd numbers, else will raise an exception. 


    try:
        number = int(input("Enter an odd number: "))
        if number % 2 == 0:
            print(f"{number} is not an odd number")
        else:
            print(f"{number} is an odd number")
    except exception as e:
        print(e)



    