# Name: Jahanzaib Qureshi
# Course: IT410
# Assignment: College records for instructors and students


# ---------- Validator class ----------
# Holds every method used to check what the user types in.
class Validator():
    """Methods that validate the information entered for each individual"""

    def __init__(self):
        """The validator doesn't need any starting data"""
        # Characters that are never allowed in a name or an email address
        self.forbidden_name_characters = '!"@#$%^&*()_=+,<>/?;:[]{}\\'
        self.forbidden_email_characters = '!"\'#$%^&*()=+,<>/?;:[]{}\\'

    def isValidEmail(self, email):
        """Check that an email is required, mostly alphanumeric, and has no forbidden characters"""
        # Required: can't be empty
        if email == "":
            return False

        # Can't contain any forbidden characters or spaces
        for character in email:
            if character in self.forbidden_email_characters or character.isspace():
                return False

        # Must have exactly one @ with text on both sides of it
        if email.count("@") != 1:
            return False
        local_part, domain = email.split("@")
        if local_part == "" or domain == "":
            return False

        # The domain needs a dot with text around it (like school.edu)
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

    def isValidId(self, id_text, max_digits):
        """Check that an ID is required, only digits, and no longer than max_digits"""
        if id_text == "":
            return False
        if not id_text.isdigit():
            return False
        if len(id_text) > max_digits:
            return False
        return True

    def isValidName(self, name):
        """Check that a name is required, made up of letters, and has no forbidden characters"""
        # Required: can't be empty
        if name == "":
            return False

        # Can't contain any forbidden characters
        for character in name:
            if character in self.forbidden_name_characters:
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

    def isValidPersonType(self, person_type):
        """Check that the type is either instructor or student"""
        if person_type == "instructor" or person_type == "student":
            return True
        return False

    def isValidRequiredText(self, text):
        """Check that a required text answer isn't empty"""
        if text == "":
            return False
        return True

    def isValidYesNo(self, answer):
        """Check that an answer is yes or no"""
        if answer == "yes" or answer == "no":
            return True
        return False


# ---------- Person, Student, and Instructor classes ----------
# Person holds what students and instructors have in common (inheritance).
class Person():
    """A parent class for anyone in the college records"""

    def __init__(self, name, email, id_number):
        """Store the name, email, and ID number"""
        self.name = name
        self.email = email
        self.id_number = id_number

    def displayInformation(self):
        """Print the information every person has"""
        print("Name: " + self.name)
        print("Email: " + self.email)


class Student(Person):
    """A student, who also has a program of study"""

    def __init__(self, name, email, id_number, program_of_study):
        """Set up the parent information, then add the program of study"""
        super().__init__(name, email, id_number)
        self.program_of_study = program_of_study

    def displayInformation(self):
        """Print all of the information for a student"""
        print("Type: Student")
        print("Student ID: " + self.id_number)
        super().displayInformation()
        print("Program of Study: " + self.program_of_study)


class Instructor(Person):
    """An instructor, who also has a last institution and highest degree"""

    def __init__(self, name, email, id_number, last_institution, highest_degree):
        """Set up the parent information, then add the education information"""
        super().__init__(name, email, id_number)
        self.last_institution = last_institution
        self.highest_degree = highest_degree

    def displayInformation(self):
        """Print all of the information for an instructor"""
        print("Type: Instructor")
        print("Instructor ID: " + self.id_number)
        super().displayInformation()
        print("Last Institution Graduated From: " + self.last_institution)
        print("Highest Degree Earned: " + self.highest_degree)


# ---------- Functions that keep asking until the answer is valid ----------
validator = Validator()


def askForEmail():
    """Keep asking until the user enters a valid email address"""
    while True:
        email = input("Email address: ").strip()
        if validator.isValidEmail(email):
            return email
        print("That email isn't valid. It is required, needs one @ and a domain like school.edu, "
              "and can't contain special characters like ! \" ' # $ % ^ & * ( ) = + , < > / ? ; : [ ] { } \\")


def askForId(label, max_digits):
    """Keep asking until the user enters a number with no more than max_digits digits"""
    while True:
        id_text = input(label + " (numbers only, up to " + str(max_digits) + " digits): ").strip()
        if validator.isValidId(id_text, max_digits):
            return id_text
        print("That ID isn't valid. It is required and must be a number with " + str(max_digits) + " digits or fewer.")


def askForName():
    """Keep asking until the user enters a valid name"""
    while True:
        name = input("Full name: ").strip()
        if validator.isValidName(name):
            return name
        print("That name isn't valid. It is required, must be letters, and can't contain special characters "
              "like ! \" @ # $ % ^ & * ( ) _ = + , < > / ? ; : [ ] { } \\")


def askForRequiredText(prompt):
    """Keep asking until the user types something"""
    while True:
        text = input(prompt).strip()
        if validator.isValidRequiredText(text):
            return text
        print("This answer is required. Please enter a value.")


def askForPersonType():
    """Keep asking until the user says instructor or student"""
    while True:
        person_type = input("Is this person an instructor or a student? ").strip().lower()
        if validator.isValidPersonType(person_type):
            return person_type
        print("Please enter either instructor or student.")


def askForYesNo(prompt):
    """Keep asking until the user answers yes or no"""
    while True:
        answer = input(prompt).strip().lower()
        if validator.isValidYesNo(answer):
            return answer
        print("Please enter yes or no.")


# ---------- Main program ----------
# Every individual entered gets added to this list as a class instance
college_records = []

keep_going = "yes"
while keep_going == "yes":
    person_type = askForPersonType()

    if person_type == "student":
        # Students need a student ID (7 digits or fewer) and a program of study
        id_number = askForId("Student ID", 7)
        program_of_study = askForRequiredText("Program of study: ")
        name = askForName()
        email = askForEmail()
        college_records.append(Student(name, email, id_number, program_of_study))
    else:
        # Instructors need an instructor ID (5 digits or fewer), last institution, and highest degree
        id_number = askForId("Instructor ID", 5)
        last_institution = askForRequiredText("Last institution graduated from: ")
        highest_degree = askForRequiredText("Highest degree earned: ")
        name = askForName()
        email = askForEmail()
        college_records.append(Instructor(name, email, id_number, last_institution, highest_degree))

    # Ask whether to keep going before the next loop
    keep_going = askForYesNo("Add another individual? (yes/no): ")

# ---------- Print every record that was collected ----------
print("\nCollege Records")
print("---------------")
if len(college_records) == 0:
    print("No records were entered.")
for record in college_records:
    record.displayInformation()
    print()
