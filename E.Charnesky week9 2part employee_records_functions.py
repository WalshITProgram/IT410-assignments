# Name: Jahanzaib Qureshi
# Course: IT410
# Assignment: Gather up to 5 employees' information (list of dictionaries),
#             reorganized so every repeated piece of logic lives in one function

# ---------- Small helper functions ----------
# Each helper does exactly one job and only uses the values passed to it.
# They are shared by all of the validation functions below, so the same
# loop is never written more than once.

def containsForbiddenCharacter(passed_text, passed_forbidden_characters):
    """Return True if any character in passed_text is in the forbidden list"""
    for character in passed_text:
        if character in passed_forbidden_characters:
            return True
    return False


def containsWhitespace(passed_text):
    """Return True if passed_text has any space, tab, etc. in it"""
    for character in passed_text:
        if character.isspace():
            return True
    return False


def isPrimarilyAlphanumeric(passed_text):
    """Return True if more than half of the characters (not counting spaces) are letters or numbers"""
    alphanumeric_count = 0
    character_count = 0
    for character in passed_text:
        if not character.isspace():
            character_count = character_count + 1
            if character.isalnum():
                alphanumeric_count = alphanumeric_count + 1
    return alphanumeric_count > character_count / 2


# ---------- Validation functions ----------
# Each function returns True when the value is valid and False when it isn't.

def isValidAddress(passed_address):
    """Address (only checked when one was entered): mostly alphanumeric, no forbidden characters"""
    if containsForbiddenCharacter(passed_address, '!"\'@$%^&*_=+<>?;:[]{}'):
        return False
    return isPrimarilyAlphanumeric(passed_address)


def isValidEmail(passed_email):
    """Email: required, no forbidden characters or spaces, one @, a domain with a dot, mostly alphanumeric"""
    # Required: can't be empty
    if passed_email == "":
        return False

    # No forbidden characters and no spaces
    if containsForbiddenCharacter(passed_email, '!"\'#$%^&*()=+,<>/?;:[]{}\\') or containsWhitespace(passed_email):
        return False

    # Must have exactly one @ with text on both sides, and a dot in the domain (like school.edu)
    if passed_email.count("@") != 1:
        return False
    local_part, domain = passed_email.split("@")
    if local_part == "" or domain == "":
        return False
    if "." not in domain or domain.startswith(".") or domain.endswith("."):
        return False

    return isPrimarilyAlphanumeric(passed_email)


def isValidId(passed_id):
    """Employee ID: required, digits only, 7 digits or fewer"""
    if passed_id == "":
        return False
    if not passed_id.isdigit():
        return False
    if len(passed_id) > 7:
        return False
    return True


def isValidName(passed_name):
    """Name: required, only letters plus spaces, hyphens, apostrophes, and periods"""
    # Required: can't be empty
    if passed_name == "":
        return False

    # Any other character (digits, @, #, etc.) makes the name invalid,
    # so there is no need for a separate list of forbidden characters
    letter_count = 0
    for character in passed_name:
        if character.isalpha():
            letter_count = letter_count + 1
        elif character not in " -'.":
            return False

    # Needs at least one actual letter
    return letter_count > 0


def isValidField(passed_field_name, passed_value):
    """Send a value to the correct validation function based on which field it belongs to"""
    if passed_field_name == "employee_id":
        return isValidId(passed_value)
    elif passed_field_name == "employee_name":
        return isValidName(passed_value)
    elif passed_field_name == "employee_email":
        return isValidEmail(passed_value)
    elif passed_field_name == "employee_address":
        # The address is optional: blank is fine, but anything typed must be valid
        return passed_value == "" or isValidAddress(passed_value)
    return False


# ---------- Functions that gather data ----------
# gatherField is the one place where the "ask, validate, ask again" loop is written.
# It keeps asking (while True) and only returns once the answer passes validation.

def gatherField(passed_field_name, passed_prompt, passed_error_message):
    """Keep asking until the answer for the given field is valid, then return it"""
    while True:
        answer = input(passed_prompt).strip()
        if isValidField(passed_field_name, answer):
            return answer
        print(passed_error_message)


def askForId():
    """Gather the employee ID"""
    return gatherField("employee_id", "Employee ID (numbers only, up to 7 digits): ",
                       "Invalid ID. It is required and must be a number with 7 digits or fewer.")


def askForName():
    """Gather the employee name"""
    return gatherField("employee_name", "Employee Name: ",
                       "Invalid name. It is required, must be letters, and can't contain special characters.")


def askForEmail():
    """Gather the employee email address"""
    return gatherField("employee_email", "Employee Email Address: ",
                       "Invalid email. It is required, must have an @ and a domain, and can't contain special characters.")


def askForAddress():
    """Gather the employee address (optional)"""
    return gatherField("employee_address", "Employee Address (optional, press Enter to skip): ",
                       "Invalid address. If provided, it must be mostly letters and numbers and can't contain special characters.")


def askForYesNo(passed_prompt):
    """Keep asking until the user answers yes or no"""
    while True:
        answer = input(passed_prompt).strip().lower()
        if answer == "yes" or answer == "no":
            return answer
        print("Please enter yes or no.")


def gatherEmployee():
    """Gather every piece of data for one employee and return it as a dictionary"""
    employee_id = askForId()
    employee_name = askForName()
    employee_email = askForEmail()
    employee_address = askForAddress()

    # Keep the same keys for every employee, even when no address was given
    if employee_address == "":
        employee_address = "No address provided"

    return {
        'employee_id': employee_id,
        'employee_name': employee_name,
        'employee_email': employee_email,
        'employee_address': employee_address
    }


# ---------- Main program ----------
# All of the dictionaries go in one list, so the list works like a database table
# with one row per employee.
MAX_EMPLOYEES = 5
employee_records = []

# Keep collecting employees until we reach 5 or the user says they're done
while len(employee_records) < MAX_EMPLOYEES:
    print("\nEmployee " + str(len(employee_records) + 1) + " of up to " + str(MAX_EMPLOYEES))

    # One function call gathers and validates everything about one employee
    employee_records.append(gatherEmployee())

    # After each employee (unless we just hit the limit), ask whether to add another
    if len(employee_records) < MAX_EMPLOYEES:
        if askForYesNo("Add another employee? (yes/no): ") == "no":
            break
    else:
        print("\nThe maximum of " + str(MAX_EMPLOYEES) + " employees has been reached.")

# ---------- Print the final list ----------
print("\nFinal employee records:")
print(employee_records)
