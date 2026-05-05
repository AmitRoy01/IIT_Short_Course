# Creating a tuple
info = ("Alice", 25, "Engineer")

# Accessing items works just like lists
print(info)               # Output: ('Alice', 25, 'Engineer')
print(info[0])            # Output: Alice (first item) 

# Access through loop
print("Info: ")
for item in info:
    print(item)

# Packing and Unpacking 
person = ("Bob", 30, "Doctor")    # Packing
name, age, job = person           # Unpacking

print(name)                  # Output: Bob
print(job)                   # Output: Doctor

birthdate = ("2002", "April", "26")
for item in birthdate:
    print(item)

year, month, date = birthdate

print(year)
print(month)
print(date)