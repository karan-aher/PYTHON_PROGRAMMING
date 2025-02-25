# Demonstrating the use of 'continue', 'pass', 'break', and 'else' in loops

# 1. 'continue' statement
print("Using 'continue' statement:")
for i in range(1, 6):
    if i == 3:  # When i is 3, skip this iteration and continue with the next one
        print("Skipping 3")
        continue
    print(f"Number: {i}")

# 2. 'pass' statement
print("\nUsing 'pass' statement:")
for i in range(1, 6):
    if i == 2:  # When i is 2, do nothing and move to the next iteration
        print("Nothing happening for 2")
        pass  # 'pass' does nothing, just moves to the next iteration
    else:
        print(f"Number: {i}")

# 3. 'break' statement
print("\nUsing 'break' statement:")
for i in range(1, 6):
    if i == 4:  # When i is 4, break the loop and exit
        print("Breaking the loop at 4")
        break
    print(f"Number: {i}")

# 4. 'else' statement with a loop
print("\nUsing 'else' with loop:")
for i in range(1, 6):
    print(f"Number: {i}")
else:
    print("This else block runs after the loop completes normally without 'break'.")

# Demonstrating 'else' with 'break'
print("\nUsing 'else' with 'break':")
for i in range(1, 6):
    print(f"Number: {i}")
    if i == 3:
        print("Breaking the loop at 3")
        break
else:
    print("This else block won't run because the loop was interrupted with 'break'.")