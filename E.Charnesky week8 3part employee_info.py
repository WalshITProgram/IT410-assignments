# Name: Jahanzaib Qureshi
# Course: IT410
# Assignment: Gather employee information with input validation

import sys

# ---------- Validation functions ----------
# Each function returns True when the value is valid and False when it isn't.

def isValidAddress(address):
    """Check an address (only called when one was entered): mostly alphanumeric, no forbidden characters"""
    # Characters that can't appear in an address
    forbidden_characters = '!"\'@$%^&*_=+<>?;:[]{}'
    for character in address:
        if character in forbidden_characters:
            return False

    # Primarily alphanumeric: more than half of the characters (not counting spaces)
    # must be letters or numbers
    alphanumeric_count = 0
    character_count = 0
    for character in address:
        if not character.isspace():
            character_count = character_count + 1
            if character.isalnum():
                alphanumeric_count = alphanumeric_count + 1
    if alphanumeric_count <= character_count / 2:
        return False

    return True


def isValidEmail(email):
    """Check an email: required, mostly alphanumeric, no forbidden characters"""
    # Required: can't be empty
    if email == "":
        return False

    # Characters that can't appear in an email address (spaces aren't allowed either)
    forbidden_characters = '!"\'#$%^&*()=+,<>/?;:[]{}\\'
    for character in email:
        if character in forbidden_characters or character.isspace():
            return False

    # Must have exactly one @ with text on both sides, and a dot in the domain (like school.edu)
    if email.count("@") != 1:
        return False
    local_part, domain = email.split("@")
    if local_part == "" or domain == "":
        return False
    if "." not in domain or domain.startswith(".") or domain.endswith("."):
        return False

    # Primarily alphanumeric: more than half of the characters must be letters or numbers
    alphanumeric_count = 0
    for character in email:
        if character.isalnum():
            alphanumeric_count = alphanumeric_count + 1
    if alphanumeric_count <= len(email) / 2:
        return False

    return True


def isValidId(employee_id):
    """Check an employee ID: required, digits only, 7 digits or fewer"""
    if employee_id == "":
        return False
    if not employee_id.isdigit():
        return False
    if len(employee_id) > 7:
        return False
    return True


def isValidName(name):
    """Check a name: required, made up of letters, no forbidden characters"""
    # Required: can't be empty
    if name == "":
        return False

    # Characters that can't appear in a name
    forbidden_characters = '!"@#$%^&*()_=+,<>/?;:[]{}\\'
    for character in name:
        if character in forbidden_characters:
            return False

    # Primarily letters: only letters plus spaces, hyphens, apostrophes, and periods are allowed
    letter_count = 0
    for character in name:
        if character.isalpha():
            letter_count = letter_count + 1
        elif character not in " -'.":
            return False

    # Needs at least one actual letter
    if letter_count == 0:
        return False

    return True


# ---------- Gather and validate the information ----------
# If anything is entered incorrectly, the program prints a message and stops (sys.exit)
# without asking for any more information.

employee_id = input("Employee ID: ").strip()
if not isValidId(employee_id):
    print("Invalid Employee ID. The ID is required and must be a number with 7 digits or fewer. Program terminated.")
    sys.exit()

employee_name = input("Employee Name: ").strip()
if not isValidName(employee_name):
    print("Invalid Employee Name. The name is required, must be letters, and can't contain special characters. Program terminated.")
    sys.exit()

employee_email = input("Employee Email Address: ").strip()
if not isValidEmail(employee_email):
    print("Invalid Email Address. The email is required, must have an @ and a domain, and can't contain special characters. Program terminated.")
    sys.exit()

# The address is optional: it is only validated when something was entered
employee_address = input("Employee Address (optional, press Enter to skip): ").strip()
if employee_address != "" and not isValidAddress(employee_address):
    print("Invalid Address. If provided, it must be mostly letters and numbers and can't contain special characters. Program terminated.")
    sys.exit()

# ---------- Print the final message ----------
message = "Hello, " + employee_name + ". Your Employee ID is " + employee_id + ", and your email address is " + employee_email + ". "

if employee_address != "":
    message = message + "Your address is " + employee_address
else:
    message = message + "You did not provide an address."

print(message)
