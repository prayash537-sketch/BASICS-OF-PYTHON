# While Loop
count = 1
while count <= 100 :
    print(count)
    count += 1
#numbers from 100 t0 1   
i = 100
while i>=1:
    print(i)
    i -= 1
#table of n using while loop
n = int(input("Enter the number : "))
i=1
while i <= 10 :
    print(n * i)
    i += 1

nums = [1,4,9,16,25,36,49,64,81,100]
i = 0
while i <= len(nums)-1:
    print(nums[i])
    i += 1

nums = (1,4,9,16,25,36,49,64,81,100)
x = int(input("Enter a number : "))
i = 0
while i<len(nums):
    if(nums[i] == x):
        print("Found at idx ",i)
    i += 1

i = 1
while i <= 10:
    if(i%2 == 0):
        i += 1
        continue
    print(i)
    i += 1
#for loop
tup = (1,2,3,4,5,6,7,8,9)

for num in tup:
    print(num)

#finding a char in particular idx
str = "Prayash"

for char in str:
    if(char == "y"):
        print("y found")
        break
    print(char)
else:
    print("End")

#Finding a number at particulat idx
num = (1,4,9,16,25,36,49,64,81,100)
x = 16
idx = 0
for el in num:
    if(el == x):
        print("Found at idx", idx)
        idx += 1

# Range function
for i in range(1,101):
    print(i)

for i in range(100,0,-1):
    print(i)

for i in range(1,11):
    print(2*i)

#factorial of a number
n = int(input("Enter a number : "))
i = 1
fact = 1
while i <= n:
    fact *= i
    i += 1
print(fact)