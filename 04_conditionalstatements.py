#Read input from the user 
age = float(input("Please enter your age: ")) 
income = float(input("Please enter your monthly income: ")) 

#1. Simple 'if' statement 

if age < 18: 
    print("You are a minor.") 

# If age is less than 18, this message is displayed. 

#2. 'if-else' statement
if income >=5000:
    print(" YOU HAVE GOOD MONTHLY INCOME.") 
else:
    print("YOU HAVE LOW MONTHLY INCOME.")

#3. 'if-elif-else' statement
if age < 18:
    print("You are a minor.") 
elif age >= 18 and age < 60:
    print("You are an adult.") 
else:
    print("You are a senior citizen.")

#4. Nested 'if' statement
if income >= 3000:
    print("You have a decent income.")
    if income >= 10000:
        print("You have a high income.")
    else:
     print("You have a medium income.")
else:
   print("your income is below the threshold for this category.")


"""
    OUTPUT
    ======
    Please enter your age: 16.8
    Please enter your monthly income: 0
    You are a minor.
    YOU HAVE LOW MONTHLY INCOME.
    You are a minor.
    your income is below the threshold for this category.
"""
