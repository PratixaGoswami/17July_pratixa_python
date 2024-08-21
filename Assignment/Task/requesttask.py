import requests
url="https://fakestoreapi.com/products"

x=requests.get(url)
data=x.json()
print(data)
count=0 
for i in data:
    print(i['title'])
    print(i['price'])
    print(i['image'])
    count+=i['price']
   
print("Total price",count) 