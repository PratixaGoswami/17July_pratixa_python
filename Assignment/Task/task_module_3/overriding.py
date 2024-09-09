class tops:

    def getdata(self,id,name):
        print("ID:",id)
        print("Name:",name)
class student(tops):
    def getdata(self, id, name):
        return super().getdata(id, name)

st=student()
st.getdata(1,"pratixa") 
      
        