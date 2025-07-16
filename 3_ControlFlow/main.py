# If-Elif-Else Statement
a = 200
b = 200
if b > a:
    print("b is greater than a")
elif a == b:
    pass
else:
    print("a is greater than b")
    
# Ternary Operator
# (condition ? exprIfTrue : exprIfFalse) this syntax is used in C, Java, JavaScript, PHP but in Python it is different.
print ("Both a and b are equal" if a == b else "a is greater than b" if a > b else "b is greater than a")

# Switch Statement
lang = input("What's the programming language you want to learn? ")
match lang:
    case "JavaScript":
        print("You can become a Web Developer.")

    case "Python":
        print("You can become a Data Scientist")

    case "PHP":
        print("You can become a Backend Developer")

    case _:
        print("The language doesn't matter, what matters is solving problems.")