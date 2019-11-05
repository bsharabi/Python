obj={
  "userId": 1,
  "name": "Bob",
  "completed": False,
  "hobbies":["Music","Sport"],
  "adderss":{
      "city":"Ariel",
      "country":"Israel"
  }
}


print(obj)
print("---------------------------------------------------")
# access specific property in obj
print(obj["name"])


# edit specific property in obj
obj["name"]="Alice"

print(obj)

# delete specific property in obj
del obj["name"]

print(obj)


# get an array that each element in the array conatain the key and the value
print("--------items--------")
print(obj.items())

print("-------------for in---------------")
for x,y in obj.items():
    print("key:",x," | value:",y)


myKey1="age"
myKey2="userId"

print("-------------Check if in---------------")
# check if obj contains a key "age"
if myKey1 in obj:
    print(myKey1,obj[myKey1])
    
# check if obj contains a key "userId"
elif myKey2 in obj:
    print(myKey2,obj[myKey2])


# add a new property
obj["age"]=12

print("-------------After adding a property---------------")
print(obj)


