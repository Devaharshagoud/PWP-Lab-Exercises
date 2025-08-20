import math
degree = float(input("Enter angle in degrees: "))
radian = math.radians(degree)
print(f"{degree} degrees is equal to {radian} radians")


x = float(input("Enter value of x: "))
y = 6 * x**2 + 4 * math.sin(x)
print("y =", y)



def evaluate_functions(x):
    f = math.cos(2 * x)        
    f_prime = -2 * math.sin(2 * x)
    f_double_prime = -4 * math.cos(2 * x)  
    return f, f_prime, f_double_prime
x_value = math.pi
results = evaluate_functions(x_value)
print("f(pi) =", results[0])
print("f'(pi) =", results[1])
print("f''(pi) =", results[2])

