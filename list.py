LETS NOW LEARN ABOUT THE LIST OF THE PYTHON

marks=[99,9,98,56,45]
PRINT THE MARKS OF ALL THE VALUES
print(marks)
print(len(marks))

PRINT THE LENGTH OF THE MARKS 

print(marks[2])

THIS PRINT THE MARKST THE INDEX 2

marks[2]=99

this cahnge the value of the index  to new value
print(marks)

print(type(marks))
this print the type of the marks



WE CAN ALSO DO SLICING IN THE LIST 
SIMPLY BY PASSING SLICE START AND THE END POINT

print(marks[2:4])

num=[1,2,3]


num.append(4)
append is used to add the value at the end of the index

print(num)

num.insert(2,4)

NUM .INSERT OPERATOR IS USED TO ADD THE VALUE AT THE DESIRE INDEX


for i in range(len(num)):
    print(i, num[i])

n=[1,2,5,6,4,3,2,1]
n.sort()
print(n)

SORT VALUE IS USED TO PRINT THE VALUE IN  THE ascending ORDER

if you want to print it in the reverse order so you have to pass the

n.sort(reverse=True)
THIS PRINT THE VALUE IN THE DESCENDING ORDER

print(n)


num.reverse()

THIS REVERSE THE WHOLE LIST
print(num)



THIS IS THE USE OF THE LIST FOR THE CALCULATING THE INDEX AND ALSO THE USE OF THE  LOOP FOR THE FINDING THE VALUES 
num=[1,2,3,4,5,6]
x=5
idx=0

for i in num:
  if(i==x):
   print(idx)
   break
  idx+=1



THE PRODUCT LIST OF THE STORE USED OF THE LSIT TO  ADD OR REOME THE STORE VALUES
products = ["Milk", "Bread", "Eggs", "Juice", "Rice"]


products.append("Sugar")
print("After adding Sugar:")
print(products)


products.remove("Eggs")
print("After removing Eggs:")
print(products)


print("Number of products:", len(products))


if "Rice" in products:
    print("Rice is available")
else:
    print("Rice is not available")



print("First product:", products[0])


print("Last product:", products[-1])


products.sort()
print("Products after sorting:")
print(products)



THE BANK SYSTEM USED FOR THE  DIFFERENT VALUES DIFFERENT VALUES 

balance=[1000,2000,3000,4000,5000]
print("print all the balances \n",balance)

balance.append(6000)
print("after adding 6000 \n",balance)

balance.remove(2000)
print("after removing 2000 \n",balance)


print("maximum of the balance\n",max(balance))
print("minimum of the balance\n",min(balance))

print("total balance is\n",sum(balance))

print("the length of the balance is\n",len(balance))



# ---------------------------------------
# PYTHON LIST METHODS - PRACTICE PROGRAM
# ---------------------------------------

students = ["Ali", "Ahmed", "Muneeb", "Usman", "Hamza"]

print("Original list:")
print(students)


# 1. append()
# Add one student at the end
students.append("Bilal")

print("\nAfter append():")
print(students)


# 2. insert()
# Add a student at a specific index
students.insert(2, "Hassan")

print("\nAfter insert():")
print(students)


# 3. extend()
# Add multiple students
new_students = ["Ayesha", "Sara"]

students.extend(new_students)

print("\nAfter extend():")
print(students)


# 4. remove()
# Remove a specific student
students.remove("Usman")

print("\nAfter remove():")
print(students)


# 5. pop()
# Remove the last student
removed_student = students.pop()

print("\nStudent removed using pop():")
print(removed_student)

print("List after pop():")
print(students)


# 6. pop(index)
# Remove student at a specific index
removed_student = students.pop(2)

print("\nStudent removed from index 2:")
print(removed_student)

print("List after pop(2):")
print(students)


# 7. index()
# Find the index of a student
position = students.index("Muneeb")

print("\nIndex of Muneeb:")
print(position)


# 8. count()
# Count how many times a student appears
students.append("Ali")
students.append("Ali")

print("\nList after adding Ali twice:")
print(students)

print("Number of times Ali appears:")
print(students.count("Ali"))


# 9. sort()
# Sort students alphabetically
students.sort()

print("\nAfter sort():")
print(students)


# 10. reverse()
# Reverse the list
students.reverse()

print("\nAfter reverse():")
print(students)


# 11. copy()
# Create a copy of the list
students_copy = students.copy()

print("\nCopied list:")
print(students_copy)


# 12. clear()
# Remove everything from the copied list
students_copy.clear()

print("\nAfter clear():")
print(students_copy)

print("\nOriginal list is still:")
print(students)


---------------------------------------
OTHER USEFUL LIST OPERATIONS
---------------------------------------

len()
print("\nNumber of students:")
print(len(students))


Check if a student exists
if "Muneeb" in students:
    print("\nMuneeb is present")


Check if a student does NOT exist
if "Zain" not in students:
    print("Zain is not in the list")


Indexing
print("\nFirst student:")
print(students[0])

print("Last student:")
print(students[-1])


Slicing
print("\nFirst three students:")
print(students[0:3])


Loop through the list
print("\nAll students:")

for student in students:
    print(student)


