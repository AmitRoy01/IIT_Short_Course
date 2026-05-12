# Setting "Guest" as the default value for the 'name' parameter
def greet(name="Guest"):
    print("Welcome,", name)

# Calling without providing an argument (Python uses the default "Guest")
greet()

# Calling with an argument (Overrides the default value)
greet("Amit")