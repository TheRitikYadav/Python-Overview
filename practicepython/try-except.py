

# Error are reflected in the except block else it does not run.
try:
    with open("./file.txt", "r+") as f:
        content = f.read()  # Might raise FileNotFoundError
except (FileNotFoundError, PermissionError) as e:
    print(f"An error occurred: {e}")


#Finally run anyway - It's like ending     
try:
    user_input = int(input("Enter an integer: "))
    print(f"You entered: {user_input}")
except ValueError:
    print("Invalid input! Please enter a valid integer.")
finally:
    print("End of input process.")


# We want valid input anyway from user.

while True:
    try:
        user_input = int(input("Enter an integer: "))
        print(f"You entered: {user_input}")
        break  # Exit the loop if input is valid
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        




