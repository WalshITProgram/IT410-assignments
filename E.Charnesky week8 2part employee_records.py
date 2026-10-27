# Name: Jahanzaib Qureshi
# Course: IT410
# Assignment: Employee data lists, hourly rates, and raises (Week 8: combined into a list of dictionaries)

# ---------- Requirement 1 ----------
# One list holding all of the exported employee data, in the order provided
employee_data = [
    1121, "Jackie Grainger", 22.22,
    1122, "Jignesh Thrakkar", 25.25,
    1127, "Dion Green", 28.75, False,
    24.32, 1132, "Jacob Gerber",
    "Sarah Sanderson", 23.45, 1137, True,
    "Brandon Heck", 1138, 25.84, True,
    1152, "David Toma", 22.65,
    23.75, 1157, "Charles King", False,
    "Jackie Grainger", 1121, 22.22, False,
    22.65, 1152, "David Toma"
]

# ---------- Requirement 2 ----------
# Sort the data into three lists: employee numbers, names, and hourly wages
employee_numbers = []
employee_names = []
hourly_wages = []

# ---------- Requirement 3 ----------
# Each value is only added if it isn't already in its list, so no duplicates get in.
# type(...) is used instead of isinstance because True and False count as ints in Python,
# and the extra True/False values need to be ignored.
for value in employee_data:
    if type(value) is int:
        if value not in employee_numbers:
            employee_numbers.append(value)
    elif type(value) is str:
        if value not in employee_names:
            employee_names.append(value)
    elif type(value) is float:
        if value not in hourly_wages:
            hourly_wages.append(value)
    else:
        # Anything else (the True/False values) is ignored on purpose
        pass

print("Employee numbers: " + str(employee_numbers))
print("Employee names: " + str(employee_names))
print("Hourly wages: " + str(hourly_wages))

# ---------- Requirement 4 ----------
# Add 30% for benefits to every hourly wage (rounded to 2 decimal places)
total_hourly_rate = []
for wage in hourly_wages:
    total_hourly_rate.append(round(wage * 1.3, 2))

print("\nTotal hourly rates: " + str(total_hourly_rate))

# Find the highest total hourly rate and warn if it's over 37.30
max_total_rate = max(total_hourly_rate)
if max_total_rate > 37.30:
    print("WARNING: A total hourly rate of $" + str(max_total_rate) + " may be a budget concern.")
else:
    print("No total hourly rates are over the 37.30 budget limit.")

# ---------- Requirement 5 ----------
# Save any total hourly rate between 28.15 and 30.65 (including both ends)
underpaid_salaries = []
for rate in total_hourly_rate:
    if rate >= 28.15 and rate <= 30.65:
        underpaid_salaries.append(rate)

print("\nUnderpaid salaries: " + str(underpaid_salaries))

# ---------- Requirement 6 ----------
# Raise in dollars for each unmodified wage:
#   22 up to 24 dollars: 5%     24 up to 26 dollars: 4%     26 up to 28 dollars: 3%
#   everything else: 2%
company_raises = []
for wage in hourly_wages:
    if wage >= 22 and wage < 24:
        raise_amount = wage * 0.05
    elif wage >= 24 and wage < 26:
        raise_amount = wage * 0.04
    elif wage >= 26 and wage < 28:
        raise_amount = wage * 0.03
    else:
        raise_amount = wage * 0.02
    company_raises.append(round(raise_amount, 2))

print("\nCompany raises (in dollars): " + str(company_raises))

# ---------- Requirement 7 ----------
# Behavior of the complex condition below (four truth tests on one line):
# Flag an employee for a pay review when ALL of these are true:
#   1. their employee number is greater than 1130 (they joined more recently), AND
#   2. their name is not "David Toma" (his pay was already reviewed), AND
#   3. EITHER their hourly wage is under 25.00 OR their total hourly rate
#      is in the underpaid_salaries list.
# Otherwise, no review is needed.
print("\nPay review check:")
for index in range(len(employee_numbers)):
    employee_number = employee_numbers[index]
    employee_name = employee_names[index]
    hourly_wage = hourly_wages[index]
    total_rate = total_hourly_rate[index]

    if employee_number > 1130 and employee_name != "David Toma" and (hourly_wage < 25.00 or total_rate in underpaid_salaries):
        print(employee_name + " should be flagged for a pay review.")
    else:
        print(employee_name + " does not need a pay review.")

# ---------- Week 8: Combine the lists into a list of dictionaries ----------
# Instead of keeping five separate lists that have to stay lined up, store everything about
# one employee together in a single dictionary. Every dictionary uses the exact same
# descriptive keys, and no data (like a name) is ever used as a key, so the final list
# works like a database table where each dictionary is one row.
employee_records = []

# count_index walks through all five lists at the same time (they are all the same length
# and in the same order), so each position in the lists belongs to the same employee
count_index = 0

# A while loop keeps going until every employee has been added
while count_index < len(employee_numbers):
    # Build one dictionary (one "row") from the values at the current position in each list,
    # then append it to the list of records
    employee_records.append({
        'employee_number': employee_numbers[count_index],
        'employee_name': employee_names[count_index],
        'hourly_wage': hourly_wages[count_index],
        'total_hourly_rate': total_hourly_rate[count_index],
        'company_raise': company_raises[count_index]
    })

    # Move to the next employee so the loop eventually stops
    count_index = count_index + 1

# Print the final list of employee dictionaries
print("\nFinal employee records:")
print(employee_records)
