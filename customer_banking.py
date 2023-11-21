# Import the create_cd_account and create_savings_account functions
import savings_account as SavingsAccount
import cd_account as CDAccount

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    print("Thank you for choosing our bank to make your account(s) with!\nPlease enter in the following information for your SAVINGS ACCOUNT:\n")
    saveBalance = float(input("Balance: "))
    saveInterestRate = float(input("Interest Rate: "))
    saveMonths = int(input("Months: "))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = SavingsAccount.create_savings_account(saveBalance, saveInterestRate, saveMonths)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"\nYour account information: \nInterest Earned: ${round(interest_earned, 2)}\nUpdated Balance: ${round(updated_savings_balance, 2)}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    print("\nPlease enter in the following information for your CD ACCOUNT: \n")
    cdBalance = float(input("Balance: "))
    cdInterestRate = float(input("Interest Rate: "))
    cdMonths = int(input("Months: "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = CDAccount.create_cd_account(cdBalance, cdInterestRate, cdMonths)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"\nYour account information: \nInterest Earned: ${round(interest_earned, 2)}\nUpdated Balance: ${round(updated_cd_balance, 2)}")

if __name__ == "__main__":
    # Call the main function.
    main()