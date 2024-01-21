import random
import os
from colorama import Fore, Style, init
import time

# Initialize colorama
init()

orange = Fore.LIGHTYELLOW_EX
green = Fore.LIGHTGREEN_EX
reset = Style.RESET_ALL
os.system('clear')

# Function to display the banner
def display_banner():
    banner_text = f"""
    {orange} mmm    mm   m    m   mm     mm   m                  
         #    ##   ##  ##   ##     ##   #                     
         #   #  #  # ## #  #  #   #  #  #
         #   #mm#  # "" #  #mm#   #mm#  #
     "mmm"  #    # #    # #    # #    # #mmmmm       v1.0   
    {reset}                                          
    {orange}telegram :{reset} https://t.me/Jamaal_ahmedy
    {orange}facebook :{reset} https://www.facebook.com/jamaal.ahmedw
    """

    print(banner_text)

# Function to check the license key
def check_license():
    expected_license_key = "AJHKH99182098MH89N283"

    # Display banner
    display_banner()

    entered_license_key = input("Enter the license key: ")

    if entered_license_key == expected_license_key:
        # Clear the screen and display the banner again
        os.system('clear')
        display_banner()
        return True
    else:
        print("Invalid license key. Exiting.")
        return False

# Function to generate Somali numbers
def generate_somali_numbers(prefix, count, start_number=None):
    numbers = []
    for _ in range(count):
        if prefix == '065':
            # For prefix 065, generate 7-digit numbers
            number = f"{prefix}{random.randint(10**6, 10**7 - 1)}"
        elif prefix == '068':
            # For prefix 068, generate 7-digit numbers
            number = f"{prefix}{random.randint(10**6, 10**7 - 1)}"
        elif prefix in ['063', '061', '090']:
            # For specific prefixes, generate 7-digit numbers
            number = f"{prefix}{random.randint(10**6, 10**7 - 1)}"
        elif start_number is not None:
            # If starting from a specific digit, generate numbers with correct length
            number_length = max(7, len(str(start_number)))
            number = f"{prefix}{start_number:0{number_length - len(prefix)}}"
        else:
            # For other prefixes, generate 7 or 8-digit numbers
            number_length = random.choice([7, 8])
            number = f"{prefix}{random.randint(10 ** (number_length - 1), 10 ** number_length - 1)}"
        
        numbers.append(number)
    return numbers

# Function to write numbers to a file
def write_numbers_to_file(numbers, filename):
    with open(filename, 'w') as file:
        for number in numbers:
            file.write(number + '\n')

# Main function
def main():
    # Check the license key first
    if not check_license():
        return

    # Display prefix options
    print(f"{orange}Choose a prefix:{reset}")
    print("1. Telesom {063} ")
    print("2. somtel  {065}")
    print("3. hormuud {061}")
    print("4. golis   {090}")
    print("5. somnet  {068}")

    # Get user input for prefix and number count
    prefix_options = ['063', '065', '061', '090', '068']
    selected_prefix_index = int(input(f"{green}Enter the number corresponding to your chosen prefix: {reset}")) - 1

    if 0 <= selected_prefix_index < len(prefix_options):
        chosen_prefix = prefix_options[selected_prefix_index]
        amount_of_numbers = int(input(f"{orange}Enter the amount of numbers you want to generate: {reset}"))
        output_filename = input(f"{orange}Enter the name of the output file: {reset}")

        # Ask if the user wants to generate numbers starting from a specific digit
        start_number_choice = input(f"{orange}Do you want to generate numbers starting from a specific digit? (y/n): {reset}").lower()
        if start_number_choice == 'y':
            start_number = int(input(f"{orange}Enter the specific starting digit: {reset}"))
        else:
            start_number = None

        # Print wait message with upside-down slash
        print(f"\n{'=' * 10} Wait {'=' * 10}")
        print("Generating numbers", end='', flush=True)
        for _ in range(10):
            print("=======", end='', flush=True)
            time.sleep(0.2)  # Add a short delay to simulate processing time

        # Generate numbers and write to file
        somali_numbers = generate_somali_numbers(chosen_prefix, amount_of_numbers, start_number)
        write_numbers_to_file(somali_numbers, output_filename)

        print(f"\n{amount_of_numbers} numbers generated with the prefix {chosen_prefix}.")
        print(f"Results written to {output_filename}")
    else:
        print("Invalid prefix selection. Please choose a valid option.")

if __name__ == "__main__":
    main()

