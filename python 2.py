# 1. Create a list of 5 numbers
my_numbers = [4, 7, 8, 15, 22]

# 2. Show each number one by one
print("--- Showing each number ---")
for i in my_numbers:
    print(i)

# 3. Check if number 8 is in the list
print("\n--- Checking for number 8 ---")
if 8 in my_numbers:
    print("Yes, the number 8 is in the list!")
else:
    print("No, the number 8 is not in the list.")

# 4. Show the first and last number in the list
print("\n--- First and Last Numbers ---")
# Index 0 grabs the first item
print("First number:", my_numbers[0]) 
# Index -1 always grabs the very last item, no matter how long the list is
print("Last number:", my_numbers[-1])