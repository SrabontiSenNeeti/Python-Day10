#Python Scope
#A variable is only available from inside the region it is created. This is called scope.

#Local Scope
#A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

from re import L, L, L, L, L, L, L, L, L, L, L, L, L, A


def myfunc():
      x = 300
      print(x)

myfunc()

#the variable x is not available outside the function, but it is available for any function inside the function:
#Function Inside Function:
#The local variable can be accessed from a function within the function:

def myfunc():
    x = 1300
    def innerfunc():
        print(x)
    innerfunc()
myfunc()   

#Global Scope
#A variable created in the main body of the Python code is a global variable and belongs to the global scope.
#Global variables are available from within any scope, global and local.     
#ex:A variable created outside of a function is global and can be used by anyone:

x = 200
def myfunc():
    print(x)
myfunc()
print(x)  


#Naming Variable:
#If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function):
#Ex:
#The function will print the local x, and then the code will print the global x:

x = 100

def myfunc():
    x = 900
    print(x)
myfunc()
print(x)    
        

#Global Keyword
""" 
If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.

The global keyword makes the variable global.
"""
#ex:If you use the global keyword, the variable belongs to the global scope:

def myfunc():
    global x
    x = 400
    print(x)
myfunc()
print(x)   


def myfunc():
    global x
    x = 800
    #print(x)
myfunc()
print(x)    

''' 
Also, use the global keyword if you want to make a change to a global variable inside a function.
Ex:To change the value of a global variable inside a function, refer to the variable by using the global keyword:
'''
a = 20
def myfunc():
    global a 
    a = 30
myfunc()
print(a)    

a = 20
def myfunc():
    global a 
    a = 40
    print(a)
myfunc()
print(a)  


"""
Topic:Python NonLocal Keyword.
ex:Make a function inside a function, which uses the variable x as a non local variable:
"""
def myfunc1():
    a = "Neeti"
    def myfunc2():
        nonlocal a
        a = "Srabonti"
    myfunc2()
    return a
print(myfunc1())   

def myfunc1():
    a = "Neeti"
    def myfunc2():
        nonlocal a
        a = "Srabonti"
        myfunc2()
        return a
print(myfunc1())    

"""
The nonlocal keyword is used to work with variables inside nested functions, where the variable should not belong to the inner function.

Use the keyword nonlocal to declare that the variable is not local.
Ex:
"""
def myfunc():
    a ="Neeti"  
    def myfunc1():
        a = "Sen"
    myfunc1()
    return a
print(myfunc())  
  
  
  
#ex1:
a = 1
def confusion():
    a = 5
    return a
print(confusion()) #5
print(a)#1

#ex2:
a = 10  
def func():
    def another_func():
        return a 
    return another_func(
    L,
    L,)
print(confusion())
print(a)

#ex:3
def confusion():
    def another_conf():
        return sum
    return another_conf()
print(confusion())
print()

#ex:4
total = 0
def count():
    total = 0
    total += 1
    return total
print(count())

#ex:5
total = 0
def count():
    total = 2
    total += 1
    return total
count()
print(count())

#ex:6
total = 0
def count():
    total = 0
    total += 1
    return total
count()
print(count())

#Ex:7p       
total = 3
def count():
    global total
    total += 1
    return total
count()
print(count())


#ex:8
total = 0
def count(total):
    total += 1
    return total
print(count(count(total)))

#Ex:9
def outer():
    x = "local"
    def inner():
        nonlocal x 
        x = "non local"
        print("inner:", x)
    inner()
    print("Outer:",x)
outer()    

#ex:10
def outer():
    x = "local"
    def inner():
        nonlocal x 
        print("inner:",x) 
    inner()
    print("inner:",x)
outer()              



