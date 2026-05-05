num = 0                          # Start from 0

while num < 10:                  # Continue while less than 10
    num = num + 1                # Increment first
    
    if num % 3 == 0:             # Check if the number is a multiple of 3
        print(f"Skipping {num} (multiple of 3)")
        continue                 # Skip the rest of iteration 
        
    print(f"Processing {num}")   # Only for non multiples of 3