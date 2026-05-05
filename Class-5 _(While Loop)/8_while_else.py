count = 1

while count <= 5:                # Condition: Loop will run as long as count is less than or equal to 5
    print(f"Count is: {count}")
    count = count + 1            # Update: Increment count by 1 in each iteration
else:                            # This block executes after the while loop finishes
    print("Out from the loop!")

print("Other block!")