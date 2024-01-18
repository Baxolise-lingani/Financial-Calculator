import math

def main():
    def print_stars_line(text):
        stars = '*' * (len(text) + 4)
        print(stars)
        print(f'* {text} *')
        print(stars)

    welcome_text = "Welcome to the Financial Calculator"
    thanks_text = "Thanks for using the Financial Calculator"
    another_calculation_text = "Proceed to the Financial Calculator"
    print_stars_line(welcome_text)

    while True:
        print_stars_line(another_calculation_text)
        print("\nWhich calculation do you wish to make:")
        print("\nInvestment - to calculate the amount of interest you'll earn on interest")
        print("Bond - to calculate the amount of interest you'll have to pay on interest")
        choice = input("\nChoose either Investment or Bond from the above menu to proceed: ").upper()

        if choice == 'INVESTMENT':
            investment_input = input("\nEnter the amount of money you are depositing: R")
            investment_input = investment_input.replace(" ", "")  # Remove spaces
            investment_amount = float(investment_input)

            if investment_amount < 0:
                print("Invalid input. Investment amount cannot be negative.")
                continue

            interest_input = input("\nEnter the interest rate (%): ")
            interest_input = interest_input.replace(" ", "") # Remove spaces
            interest_rate = float(interest_input) / 100
            if interest_rate < 0:
                print("Invalid input. Annual interest cannot be negative.")
                continue
            years_input = input("\nEnter the number of years you plan on investing for: ")
            years_input = years_input.replace(" ", "") # Remove spaces
            years = int(years_input)
            if years < 0:
                print("\nInvalid input. Number of years cannot be negative.")
                continue
            interest_type = input("\nWhich interest do you prefer:\n1. Simple interest\n2. Compound interest\n\nEnter '1' or '2': ")

            if interest_type == '1':
                final_amount = investment_amount * (1 + interest_rate * years)
            elif interest_type == '2':
                final_amount = investment_amount * math.pow((1 + interest_rate), years)
            else:
                print("\nInvalid interest type. Please enter '1' or '2'.")
                continue

            print(f"Your investment will be worth: R{final_amount:.2f}")

        elif choice == 'BOND':
            present_input = input("\nEnter the present value of the house: R")
            present_input = present_input.replace(" ", "")  # Remove spaces
            present_value = float(present_input)
            if present_value < 0:
                print("\nInvalid input. Present value cannot be negative.")
                continue
            annual_interest_rate_input = input("\nEnter the annual interest rate(%): ")
            annual_interest_rate_input = annual_interest_rate_input.replace(" ", "") # Remove spaces
            annual_interest_rate = float(annual_interest_rate_input) / 100
            if annual_interest_rate < 0:
                print("\nInvalid input. Annual interest cannot be negative.")
                continue
            numberOfYears_input = input("\nEnter the number of years for bond repayment: ")
            numberOfYears_input = numberOfYears_input.replace(" ", "") # Remove spaces
            numberOfYears = int(numberOfYears_input)
            if numberOfYears < 0:
                print("\nInvalid input. Number of years cannot be negative.")
                continue
            monthly_interest_rate = annual_interest_rate / 12
            repayment = (monthly_interest_rate * present_value) / (1 - math.pow(1 + monthly_interest_rate, -(numberOfYears * 12)))

            print(f"\nYour monthly bond repayment will be: R{repayment:.2f}")

        else:
            print("\nInvalid choice. Please enter 'INVESTMENT' or 'BOND'.")
            continue

        another_calculation = input("\nDo you want to perform another calculation? (yes/no): ").lower()
        if another_calculation != 'yes':
            print_stars_line(thanks_text)
            break

if __name__ == "__main__":
    main()
