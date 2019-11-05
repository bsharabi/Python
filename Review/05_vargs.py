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
'''
def print_params(msg, *numbers, **pairs):
    global obj
    print("msg",msg)
    print("numbers",numbers)
    print("pairs",pairs)
    obj["pairs"]=pairs

print(obj)
print_params("hello",1,2,3,4,"TEST",name="bobi",age=13)
print(obj)
'''
def print_params2(msg, *numbers, **pairs):
    global obj
    print("msg",msg)
    print("numbers",numbers)
    print("pairs",pairs)
    for x,y in pairs.items():
        obj[x]=y
print(obj)
print_params2("hello",1,2,3,4,"TEST","TEST","TEST","TEST","TEST",3,5,1.5,name1="bobi",age=13)

print(obj)