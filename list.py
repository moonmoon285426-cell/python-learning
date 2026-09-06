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
