# DICTIONARY
info = {
    'Name' : 'Prayash',
    'Cgpa' : 9.6,
    'Subject' : {
        'Maths' : 90,
        'Science' : 85,
        'Nepali' : 80,
    }
}

new_info = {'Batch' : 2081}

info.update(new_info)
print(info.items())

# SET
collection = set()
collection.add(1)
collection.add(2)
collection.add(3)
collection.remove(3)
collection.clear()
print(collection)

# QUESTION
new_update = {
    'table' : ["a piece of furniture" ,"list of facts & figures"],
    'cat' : 'a small animal'
}

print(new_update)

subject = {
    'python','java','C++','python','javascript','java','python','java','C++','C'
    }
print(len(subject),"class is required for the student")

my_dic = {}
new_update = {
    'maths' : float(input("Enter the number of maths : ")),
    'science' : float(input("Enter the number of science : ")),
    'nepali' : float(input("Enter the number of nepali : ")),
}

my_dic.update(new_update)
print(my_dic)

values = {
    ("float",9.0),
    ("int",9)
}
print(values)