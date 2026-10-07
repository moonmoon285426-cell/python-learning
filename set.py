 now we  are learning about the sets and the sets only of that type

 set only deals with the immutable tupe of the data 
 in sets only the tuples and strings will be included


  in set no duplicate things will come


s={1,2,3,2,3}
print(s)

#  python print only the unique values in the set and it will not print the duplicate values

print(len(s))

s.add(5)
print(s)



numbers = {10, 20, 30, 40}

numbers.remove(30)

print(numbers)

 after removing the 30 from the set it will print the remaining values in the set order may be changed because the set is unordered collection of data and it will not maintain the order of the data in the set


s={}
print(type(s))
 an empty set is behave like the dictionary because the empty set is not a set it is a dictionary so to create an empty set we have to use the set() function




 this will print only the  empty set 

s.clear()
print(s)



 UNION and INtersection


 union method
s1={1,2,3,4,5}
s2={1,6,7,8,9}

#  for taking the union we use the union for all the elements

print(s1.union(s2))


# for taking the intersection we mostly use the intersection
print(s1.intersection(s2))
print(s2.intersection(s1))






info = [
    ("alice", "math"),
    ("bob", "science"),
    ("alice", "science"),
    ("charlie", "math"),
    ("bob", "math"),
    ("alice", "english"),
    ("charlie", "english"),
]

names = set()
subjects = set()

for name, course in info:
    names.add(name)
    subjects.add(course)

print("Unique names:", names)
print("Unique subjects:", subjects)



