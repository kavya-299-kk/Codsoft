import random
import string

def generate_password(min_length,numbers=True,special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pswd =""
    criteria_met = False
    has_number = False
    has_special = False

    while not criteria_met or len(pswd)<min_length:
        new_char = random.choice(characters)
        pswd += new_char


        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True


        criteria_met = True
        if numbers:
            criteria_met = has_number
        if special_characters:
            criteria_met = criteria_met and has_special

    return pswd         

min_length = int(input("Enter the minimum length : "))
has_number = input("Do you want to include number (y/n)?").lower() =="y"
has_special = input("Do you want to include special_characters (y/n)?").lower() == "y"

pswd = generate_password(min_length,has_number,has_special)
print("The generated password is : ",pswd)