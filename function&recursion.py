def sum(a,b):
    s = a+b
    return s
print(sum(4,5))

def avg(a,b,c):
    a = (a+b+c)/3
    return a
print(avg(1,2,3))

# QUESTIONS
cities = ["Kathmandu","Pokhara","Chitwan"]
def calc_length(list):
    print(len(list))
    return len(list)

calc_length(cities)

heroes = ["Ironman","SpiderMan","Thor"]
def print_el(list):
    for item in list:
        print(item, end=" ")
        
print_el(heroes)

# TO FIND FACTORIAL
def find_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)

find_fact(5)

# TO CONVERT USD TO NPR
amount = float(input("Enter the amount of USD : "))
def calc_npr(n):
    npr = amount * 151.03
    print(n,"USD =",npr,"NPR")

calc_npr(amount)

number = int(input("Enter a number odd/even : "))
def find_num(n):
    if(n % 2 == 0):
        print(n,"is Even")
    else:
        print(n,"is Odd")
find_num(5)

# RECURSION

def display(n):
    if(n == 0):
        return
    print(n)
    display(n - 1)
    
display(5)

# FACTORIAL USING RECURSION
def fact(n):
    if(n == 0 or n==1):
        return 1
    else:
        return n * fact(n-1)
    
print(fact(5))

# SUM OF N NATURAL NUMBER
def sum(n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return n + sum(n-1)
print(sum(int(input("Enter the value for N : "))))

nums = [1,2,3,4,5,6,7,8,9,10]
def display(list,idx):
    if(idx == len(list)):
        return
    print(list[idx])
    display(list,idx+1)
    
display(nums,0)