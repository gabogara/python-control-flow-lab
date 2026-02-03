# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

# def check_letter():
#     # Your control flow logic goes here
#     letter = input("Enter a letter (a-z or A-Z): ").strip()
#     if len(letter) !=1 or not letter.isalpha():
#         print("Invalid input. Please enter a single alphabetical letter.")
#         return

#     lower_letter = letter.lower()

#     if lower_letter in "aeiou":
#         print("The letter " + letter + " is a vowel")
#     else:
#         print("The letter " + letter + " is a consonant.")

# check_letter()

#---------------------------------------------------------------------------------------------------------
# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

# def check_voting_eligibility():
#     VOTING_AGE = 18
#     while True:
#         user_input= input("Please enter your age: ").strip()
#         if not user_input.isdigit():
#             print("Invalid input. Please enter a valid number.")
#         else: 
#             age = int(user_input)
#             if age < 0:
#                 print("Invalid age. Age cannot be negative.")
#             else:
#                 break
    
#     if age < VOTING_AGE:
#         print("You are not eligible to vote yet.")
#     else:
#         print("You are eligible to vote!")
    
# check_voting_eligibility()

#---------------------------------------------------------------------------------------------------------
# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    # Your control flow logic goes here
    while True:
        age_dog = (input("Input a dog age: "))
        if not age_dog.isdigit():
            print("Invalid input. Please enter a valid number.")
        else:
            age= int(age_dog)
            break

    if age <= 2:
        dog_years = age * 10
        print("The dog age in dog years is", dog_years)
    else:
        dog_years = 20 + (age - 2) * 7
        print("The dog age in dog years is", dog_years)

calculate_dog_years()
#--------------------------------------------------------------------------------------------------------
# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

# def weather_advice():
#     # Your control flow logic goes here
#     cold_input = input("Is it cold? (yes/no): ").strip()
#     cold = cold_input.lower()

#     raining_input = input("Is it raining? (yes/no): ").strip()
#     raining = raining_input.lower()

#     if cold == "yes" and raining == "yes":
#         print("Wear a waterproof coat.")
#     elif cold == "yes" and raining == "no":
#         print("Wear a warm coat.")
#     elif cold == "no" and raining == "yes":
#         print("Carry an umbrella.")
#     elif cold == "no" and raining == "no":
#         print("Wear light clothing.")
#     else:
#         print("Please answer with yes or no.")

# weather_advice()
#----------------------------------------------------------------------------------------------------------
# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

# def determine_season():
#     # Your control flow logic goes here
#     month = input("Enter the month of the year (Jan - Dec): ").strip()
#     day_input = input("Enter the day of the month: ").strip()

#     if not day_input.isdigit():
#         print("Invalid day. Please enter a number.")
#         return
    
    
#     day = int(day_input)
    

#     months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

#     if not month in months:
#         print("Invalid month. Please use format like Jan, Feb, ..., Dec.")
#         return
#     if day<0 or day>31:
#         print("Invalid day. Enter a value from 1 to 31.")
#         return
    
#     if (month == "Dec" and day>20) or month in ["Jan", "Feb"] or (month == "Mar" and day<20): 
#         season= "Winter"
#     elif (month == "Mar" and day>19) or month in ["Apr","May"] or (month == "Jun" and day<21): 
#         season = "Spring"
#     elif (month == "Jun" and day>20) or month in ["Jul","Aug"] or (month == "Sep" and day<22):
#         season = "Summer"
#     else:
#         season = "Fall" 
    

#     print(f" {month} {day} is in {season}")

# determine_season()
