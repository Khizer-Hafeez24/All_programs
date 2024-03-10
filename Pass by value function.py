# pass by value function
name = "Khizer"
id='01'
def my_func(name, id):
    return
print(name + id)

# function with default argument
def show_employee(name, salary=55000):
    print("Name:", name, "salary:", salary)
show_employee("Khizer Hafeez", 55000)
show_employee("Khizer Durrani")
# pass by variable
def modify_string(s):
    print("Inside modify_string, before modification, s =", s)
    s = s + " World!"
    print("Inside modify_string, after modification, s =", s)
def main():
    my_string = "Hello"
    print("Before calling modify_string, my_string =", my_string)
    modify_string(my_string)
    print("After calling modify_string, my_string =", my_string)