tup = ("C", "D", "A", "A", "B", "B", "A")
print(tup.count("A"))

list = ["C", "D", "A", "A", "B", "B", "A"]
list.sort()
print(list)

#Palindrome or not
list1 =[1,2,1]
copy_list = list1.copy()
copy_list.reverse()

if(copy_list == list1):
    print("palindrome")
else:
    print("not palidrome")

#sorting movies according to their name
movieName = [ input("Enter name of first movie :"), input("Enter name of second movie :"), input("Enter name of third movie :")]
movieName.sort()
print(movieName)


# tuple
tup = (2, 1, 3, 1, 5, 4)
print(type(tup))
print(tup[1:3])
print(tup.index(1))
print(tup.count(1))

# list method
list = [2, 1, 3]
list.insert(0, 4)
print(list)

# list slicing
marks = [85, 94, 76, 63, 48]
print(marks[-3:-1])

student = ["prayash", 24, "Kathmandu"]
print(student)

student[0]  = "Ram"
print(student)