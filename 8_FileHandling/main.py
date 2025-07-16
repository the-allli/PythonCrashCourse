f = open("demo.txt", "a")
f.write("Now the file has content!")
f.close()

f = open("demo.txt", "w")
f.write("Woops! I have Overridden the content!")
f.close()

f = open("demo.txt", "rt")
print(f.read())
f.close()

f = open("myfile1.txt", "x")
f = open("myfile2.txt", "w")

import os
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist") 