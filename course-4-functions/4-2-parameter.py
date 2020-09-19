# We can add parameter in the function
def fun_2(parameter):
    print(parameter+2)
fun_2(8)

# Default parameters
def default_example(num1=7, num2=8):
    print(num1*num2)

default_example()
default_example(4,6) #which you can re-define the parameter