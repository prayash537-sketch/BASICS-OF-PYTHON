str1 = "This is a string.\n"
str2 = "We are creating it on python"
print(len(str2))

# INDEXING
index = str2[0]
print(index)

# SLICING
str = "Prayash"
print(str[1:4])
print(str[:4])
print(str[1:])

str = "I am studying python from Youtube"
print(str.capitalize())
print(str.replace("o","a"))
print(str.find("o"))
print(str.count("o"))

name = str(input("Enter your Name : "))
length = len(name)

print(length)

sentence = str(input("Enter a word with s : "))
find = sentence.count("s")

print(find)

name = str(input("Enter your name : "))
age = int(input("Enter your age : "))

if(age>=18):
    print("You can vote ",name)
else:
    print("You cannot vote ",name)


marks = float(input("Enter your mark : "))
if(marks >= 90):
    print("Grade A")
elif(89>=marks and marks >= 80):
    print("Grade B")
elif(79>=marks and marks >= 70):
    print("Grade C")
elif(69>= marks):
    print("Grade D")

num = int(input("Enter odd/even number : "))

if(num % 2 == 0):
    print("Number is even")
else:
    print("Number is odd")

a = int(input("Enter first number"))
b= int(input("Enter second number"))
c = int(input("Enter third number"))

if(a>b and a>c):
    print(a,"is the greatest")
elif(b>a and b>c):
    print(b,"is the greatest")
else:
    print(c,"is the greatest")

checkNum = int(input("Enter a number"))
if(checkNum % 7 == 0):
    print(checkNum,"is divisible by 7")
else:
    print(checkNum,"is not divisible by 7")