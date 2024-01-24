import os

def get_input():
    # Get user input for weight and height
    while True:
        try:
            weight = float(input("Enter weight (in kg): "))
            height = float(input("Enter height (in meters): "))
            
            # Validate input: positive values for weight and height
            if weight > 0 and height > 0:
                return weight, height
            else:
                print("Please enter positive values for weight and height.")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

def calculate_bmi(weight, height):
    # Calculate BMI using the formula: BMI = weight / (height^2)
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    # Classify BMI into different categories
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def display_result(bmi, category):
    # Display the calculated BMI and its category
    print("BMI: ", round(bmi, 2))
    print("Category: ", category)

def main():
    try:
        # Get input, calculate BMI, classify, and display result
        weight, height = get_input()
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)
        display_result(bmi, category)
    except Exception as e:
        print(f"An error occurred: {e}")

while True:
    main()

    # Prompt user to continue or exit
    while True:
        ch = input("\nDo You Want To Continue? Y - yes\t N - no\n").lower()
        if ch in ('y', 'n'):
            break
        else:
            print("Wrong Choice")

    # Clear console screen if user wants to continue
    if ch == 'n':
        break
    elif ch == 'y':
        os.system('cls')  # Use 'clear' for Unix-based systems