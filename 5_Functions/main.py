print("\nFunction with default value")
def my_function(country = "Norway"):
    print("I am from " + country)
my_function("Sweden")
my_function()

print("\nFunction with key=value arguments")
def my_function(child1, child2, child3):
    print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus") 

print("\nFunction with Arbitrary Arguments")
def my_function(*kids):
    print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")

print("\nFunction with Arbitrary Keyword Arguments")
def my_function(**kid):
    print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")

print("\nLambda Function (anonymous function)")
def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))