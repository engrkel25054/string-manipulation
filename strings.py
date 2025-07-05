# Program specification
"""
Write code that asks the user to enter their
birthday in the form mm/dd/yyyy, and then prints a string of the
form ‘You were born in the year yyyy.’
"""

birthday = input("Please enter your birthday in mm/dd/yyyy format: ")
print(f"You were born in the year {birthday[6:]}.")