# Name: Jahanzaib Qureshi
# Course: IT410
# Assignment: Gather up to 5 employees' information with input validation (list of dictionaries)

# ---------- Validation functions ----------
# Each function returns True when the value is valid and False when it isn't.
# These are the same checks used in the previous assignment.

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


# ---------- Functions that keep asking until the answer is valid ----------
# Instead of ending the program on bad input, each of these loops (while True)
# and asks again. The loop only ends (return) once the answer passes validation.

def askForAddress():
    """Address is optional: blank is fine, but anything typed must be valid"""
    while True:
        address = input("Employee Address (optional, press Enter to skip): ").strip()
        if address == "" or isValidAddress(address):
            return address
        print("Invalid address. If provided, it must be mostly letters and numbers and can't contain special characters.")


def askForEmail():
    """Keep asking until a valid email is entered"""
    while True:
        email = input("Employee Email Address: ").strip()
        if isValidEmail(email):
            return email
        print("Invalid email. It is required, must have an @ and a domain, and can't contain special characters.")


def askForId():
    """Keep asking until a valid employee ID is entered"""
    while True:
        employee_id = input("Employee ID (numbers only, up to 7 digits): ").strip()
        if isValidId(employee_id):
            return employee_id
        print("Invalid ID. It is required and must be a number with 7 digits or fewer.")


def askForName():
    """Keep asking until a valid name is entered"""
    while True:
        name = input("Employee Name: ").strip()
        if isValidName(name):
            return name
        print("Invalid name. It is required, must be letters, and can't contain special characters.")


def askForYesNo(prompt):
    """Keep asking until the user answers yes or no"""
    while True:
        answer = input(prompt).strip().lower()
        if answer == "yes" or answer == "no":
            return answer
        print("Please enter yes or no.")


# ---------- Main program ----------
# Each employee is stored as a dictionary, and every dictionary uses the same descriptive keys.
# No data (like a name) is used as a key. All of the dictionaries go in one list,
# so the list works like a database table with one row per employee.
MAX_EMPLOYEES = 5
employee_records = []
employee_count = 0

# Keep collecting employees until we reach 5 or the user says they're done
while employee_count < MAX_EMPLOYEES:
    print("\nEmployee " + str(employee_count + 1) + " of up to " + str(MAX_EMPLOYEES))

    # Each answer is validated by its own function before moving on
    employee_id = askForId()
    employee_name = askForName()
    employee_email = askForEmail()
    employee_address = askForAddress()

    # Keep the same keys for every employee, even when no address was given
    if employee_address == "":
        employee_address = "No address provided"

    # Add this employee's dictionary to the list
    employee_records.append({
        'employee_id': employee_id,
        'employee_name': employee_name,
        'employee_email': employee_email,
        'employee_address': employee_address
    })
    employee_count = employee_count + 1

    # After each employee (unless we just hit the limit), ask whether to add another
    if employee_count < MAX_EMPLOYEES:
        add_another = askForYesNo("Add another employee? (yes/no): ")
        if add_another == "no":
            break
    else:
        print("\nThe maximum of " + str(MAX_EMPLOYEES) + " employees has been reached.")

# ---------- Print the final list ----------
print("\nFinal employee records:")
print(employee_records)
