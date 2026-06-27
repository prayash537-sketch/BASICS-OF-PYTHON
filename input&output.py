#READING A FILE
f = open("demo.txt","r")
data = f.read()
print(data)
print(type(data))
f.close()

#WRITING TO A FILE
f = open("demo.txt","w") #"w" overwrites the entire file
f.write("This is a new paragraph\nThis is added using python")
f.close()

#USING "r+"
f = open("demo.txt","r+")
f.write("abc")
print(f.read())
f.close()

#WITH SYNTAAX
with open("demo.txt","r") as f:
    data = f.read()
    print(data)
    
with open("demo.txt","w") as f:
    f.write("New Data")

#DELETING A FILE
import os
os.remove("demo.txt")

#QUESTIONS
#Create new file and add following data
with open("practice.txt","w") as f:
    f.write("Hi everyone\nWe are learning File I/O using Java\nI like programming in Java")

#Change Java to Python
with open("practice.txt","r") as f:
    data = f.read()
    
new_data = data.replace("Java","Python")

with open("practice.txt","w") as f:
    f.write(new_data)
    
#TO FIND A WORD IN A FILE
def check_for_word():
    word = "learning"
    with open("practice.txt","r") as f:
        data = f.read()
        if(word in data):
            print("Found")
        else:
            print("Not found")

#TO FIND LINE IN WHICH THE WORD OCCUR
def check_for_line():
    word = "programming"
    line_no = 1
    
    with open("practice.txt", "r") as f:
        for line in f:
            if word in line:
                print(line_no)
            line_no += 1

check_for_line()

count = 0
with open("practice.txt","r") as f:
    data = f.read()

    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1
            
print(count)
    