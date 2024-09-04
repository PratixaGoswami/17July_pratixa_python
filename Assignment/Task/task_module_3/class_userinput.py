class studinfo:

    def getdata(self):
            self.id=input("Enter id:")
            self.name=input("enter name:")
    def printdata(self):
          print("Id:",self.id)        
          print("id:",self.name)

st=studinfo()
st.getdata()          
st.printdata()