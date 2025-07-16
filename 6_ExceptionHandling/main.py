try:
    # code that may fail
    pass
except SomeException:
    # handle specific error
    pass
except (Error1, Error2):
    # handle multiple
    pass
except Exception as e:
    # handle any
    print(e)
else:
    # runs if no exception
    pass
finally:
    # always runs
    pass

# Raise an exception
x = int(input("Enter an Integer."))
if not type(x) is int:
    raise TypeError("Only integers are allowed") 
else:
    print(x)