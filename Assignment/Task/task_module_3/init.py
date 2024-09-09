import random
class bank:
    acno=random.randint(11111,99999)
    def __init__(self) -> None:  #constructor
        print("Account number:",self.acno)

bn=bank()        