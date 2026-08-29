the use of the for loop 


  THIS LOOP PRINT THE VALUES OF THE 12 
for var in range(12):
        print (var+1)

THS ALSO PRINT THE VALUE FROM THE 0 TO 10
for i in range(10):
    print(i) 

we can use for loop to use conditional statement in python


          THIS PRINT HOW MANY VLAUES ARE USED TO PRINT THE  
CHECKING HOW MANY VALUES ARE IN THE E
word="muneeb"
sum=0  
for i in word:
      print(i)
      
      if(i=="e"):
       sum+=1  
print("the number of e in the word is:",sum)          


THE LOOP IS USED TO PRINT THE VOWEL IN THE WORDS

word="artificalintelligence"
count=0
for i in word:
      if(i=='a'or i=='e' or i=='i' or i=='o' or i=='u'):
         count+=1
print("the number of vowels in the word is:",count)   



THIS PRINT HOW MANY VALUES ARE IN THE  AND

BREAK IS USED TO STOP THE VALUES AT THE FIXED POINT
for i in range(10):
      if(i==5):
            break
      print(i)


continue value skip that iteration which is at that position
for i in range(10):
      if(i==5):
            print("the value of i is 5 and the loop will be continued")
            continue
 
      print(i)

THIS PRINT THE VALUES OF THE TABLES
num=1
for i in range(10):
      print(num,"*",i,"=",num*i

IN THE RANGE FUNCTION  FIRST VALUE IS THE VALUE OF THE STARTING INDEX AND THEN MIDDLE FOR THE STOPPING INDEX AND THEN THE LAST FOR THE SKIPING TO SKIP HOW MUCH VALUES 
for i in range(5,10,1):
    print(i)

NOW THE SPACING VALUES IS 2 
for i in range(5,10,2):
    print(i)

PRINTING THE SUM OF THE FIRST FIVE NATURAL NUMBERS
sum=0
for i in range(1,5):
    sum+=i
    print("the sum of the first",i,"natural number is:",sum)


             n=int(input("enter the value of the n:"))

            ROUGH EXAMPLE
sum=0
for i in range(2,n+1,2):
    sum+=i
    print("the work is going in")   
print("the sumof the ",sum)



