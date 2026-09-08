NOW WE WILL LEARN ABOUT THE DICTIONARY 

DICTIONARY WORK IN THE PAIR WE HAVE THE TWO VALUES IN THE FORM OF THE PAIRS
KEY VALUES PAIRS

info={
      "name":"kala",
      "cgpa":9.6,
      "subjects":["maths","computer science"]
      
}
print(info)
print(info["name"], info["cgpa"], info["subjects"])



 WE CAN DELETE THE VALUES FROM THE DICTIONARY

del info["cgpa"]
print(info)


USE OF THE GET FUNCTION FOR GETTING THE VALUE WHICH IS NOT GIVEN OR NOT ASSIGNEDD IN THE DICTIONARY

print(info.get("value"))

THIS WILL PRINT THE NONE 


WE USE THE KEY FUNCTION FOR GETTING THE VALUES  OF THE KEY OF THE WHOLE DICTIONARY


print(info.key())

print(info.values())

 THIS WILL PRINT THE KEY VALUES FOR THE WHOLE DICTIONARY


print(info.items())

THIS WILL PRINT THE BOTH VALUES AND THE KEY PAIRS







