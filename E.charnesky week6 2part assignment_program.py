# ---------- Requirement 1 ----------
# Store first name in all lowercase letters
first_name = "jahanzaib"

# ---------- Requirement 2 ----------
# Store last name in all uppercase letters
last_name = "QURESHI"

# ---------- Requirement 3 ----------
# Print the greeting with the first name in uppercase and the last name in lowercase
print("Hello, " + first_name.upper() + " " + last_name.lower())

# ---------- Requirement 4 ----------
# Print two newlines (end="" stops print() from adding a third one)
print("\n\n", end="")

# ---------- Requirement 5 ----------
# Print the quote with quotation marks at the beginning and end
# The \" escapes let us print double quotes inside a double-quoted string
print("\"Start by doing what's necessary; then do what's possible; and suddenly you are doing the impossible - Francis of Assisi\"")

# ---------- Requirement 6 ----------
# Store two decimal numbers
first_number = 8.5
second_number = 2.5

# ---------- Requirement 7 ----------
# Store the result of each operation in its own variable
addition_result = first_number + second_number
subtraction_result = first_number - second_number
multiplication_result = first_number * second_number
division_result = first_number / second_number

# ---------- Requirement 8 ----------
# Print each result on its own line (str() converts the numbers so they can be joined with text)
print(str(first_number) + " plus " + str(second_number) + " equals " + str(addition_result))
print(str(first_number) + " minus " + str(second_number) + " equals " + str(subtraction_result))
print(str(first_number) + " times " + str(second_number) + " equals " + str(multiplication_result))
print(str(first_number) + " divided by " + str(second_number) + " equals " + str(division_result))

# ---------- Requirement 9 ----------
# Store the current month as a string and the day of the month as a number
current_month = "November"
current_day = 12

# ---------- Requirement 10 ----------
# \n starts a new line and each \t tabs over once, so \t\t tabs over two times
print("\n\t\tToday is day " + str(current_day) + " of the month of " + current_month + ".")
