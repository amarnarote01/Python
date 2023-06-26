# closure :-one function returens the another function 

# def outer_fun(msg):
#     print("I am in outer fun block")
#     def inner_fun():
#         print("I am in innerfun block")
#         print(msg)
#     return inner_fun
# var=outer_fun("Hi students")
# var()

# def outer_fun(b):
#     print("I am in outer fun")
#     def inner_fun(a):
#         print("Value of a:-",a)
#         print("Value of b:-",b)
#     return inner_fun
# result = outer_fun(10)
# result(20)

# ---------------------------------------------
# def to_power(x):
#     def calc_power(n):
#         return n**x
#     return calc_power
# cube=to_power(3)
# print(cube(2))
# -----------------------------------------------
# decorators:- enhance the functinality of other functions
# syntax- @decorator_name
# def decorator_function(any_function):
#     def wrapper_function():
#         print("This is awesome function")
#         any_function()
#     return wrapper_function
# @decorator_function
# def func1():
#     print("I am in func1")
    
# func1()
# var =decorator_function(func1)
# var()