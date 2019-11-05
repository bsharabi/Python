obj=[{
  "userId": 1,
  "name": "Bob",
  "completed": False,
  "hobbies":["Music","Sport"],
  "adderss":{
      "city":"Ariel",
      "country":"Israel"
  }
},{
  "userId": 2,
  "name": "Alice",
  "completed": False,
  "hobbies":["Music","Sport"],
  "adderss":{
      "city":"Ariel",
      "country":"Israel"
  }
}]



# get an array that each element in the array conatain the key and the value
print("--------items--------")
print(obj[0].items())

print("-------------for in---------------")
for x in range(2):
    for x,y in obj[x].items():
        print("key:",x," | value:",y)


myKey1="age"
myKey2="userId"

print("-------------Check if in---------------")
for x in range(2):
    # check if obj contains a key "age"
    if myKey1 in obj[x]:
        print(myKey1,obj[x][myKey1])
        
    # check if obj contains a key "userId"
    elif myKey2 in obj[x]:
        print(myKey2,obj[x][myKey2])


# add a new property
for x in range(2):
    obj[x]["age"]=12

print("-------------After adding a property---------------")
print(obj)

obj[0]["kaki"]="bbai" # insert into the obj a key and value

print(obj)