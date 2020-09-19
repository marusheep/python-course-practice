# =====variable scope===
# global scope is the variable out of the function and local scope is the variable in the function.

varExample = "hello, world" # global scope

def loc_fun():
    varExample = "this is a string."
    return varExample  # local scope

print(varExample)
print(loc_fun())

# 1. local variables cannot be used by code in the global scope.
# 2. global variables can be accessed by code in the local scope.
# 3. the local scope of one function can't use variables from another function's local scope

# Global Statement
def loc_ex():
    global fruit #which is global statement that makes local function can be used as aglobal variable.
    fruit = "pear"
    print(fruit)

fruit = "apple"
loc_ex()
print(fruit)


