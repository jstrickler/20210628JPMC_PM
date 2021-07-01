
x = 100  # GLOBAL variable -- visible from here to end of file

def spam():
    x = "Bob"  # LOCAL!!
    y = 42   # LOCAL variable -- only visible in function
    print("in spam(): x is", x)

x = "wombat"

spam()
print("Main: x is", x)

