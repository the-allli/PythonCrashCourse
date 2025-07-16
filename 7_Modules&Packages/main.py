import mymodule
from mymodule import greet
from mymodule import greet as custom_greet
from mymodule import *

print(mymodule.greet("Ahmad"))

from mypackage import module1
print(module1.greet("Ali"))

from mypackage.module2 import greet
