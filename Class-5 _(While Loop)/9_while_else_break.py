count = 1

while count <= 5:                # Condition: Loop will run as long as count is less than or equal to 5
    print(f"Count is: {count}")
    count = count + 1            # Update: Increment count by 1 in each iteration       
    if count == 3:               # Check if count is equal to 3
        print("Breaking out of the loop at count 3!")
        break                     # Exit the loop immediately when count is 3
else:                            # This block executes if the loop completes without being broken
    print("Out from the loop!")

