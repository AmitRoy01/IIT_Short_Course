def scquare(x):
    return x * x   
result = scquare(5)

print("The square of 5 is:", result)


# Function that calculates and returns a value instead of printing it directly
def multiply(a, b):
    return a * b

# Storing the returned value in a variable named 'result'
result = multiply(4, 5)
print("The multiplication result is:", result)


def get_marks():
    x = 10
    y = 20
    return x, y

result = get_marks()

print (result)
print (result[0])
print (result[1])
