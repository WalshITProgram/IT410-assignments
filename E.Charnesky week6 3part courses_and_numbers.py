# Name: Jahanzaib Qureshi
# Course: IT410
# Assignment: Course lists and numbers divisible by 6
# Date: November 12, 2026

# ---------- Requirement 1 ----------
# List of courses taken at Walsh College, all lowercase
walsh_courses = [
    "mth300",
    "it417",
    "ecn201",
    "ids400",
    "it410",
]

# ---------- Requirement 2 ----------
# Sort the list, then print each course in uppercase with the message
walsh_courses.sort()
for course in walsh_courses:
    print("I have taken " + course.upper() + " at Walsh College.")

# ---------- Requirement 3 ----------
# Save a copy of the courses I've already taken so I can remove them later (requirement 4)
courses_already_taken = walsh_courses[:]

# Add courses planned for next term, then re-sort
upcoming_courses = ["it420", "it430"]
for upcoming_course in upcoming_courses:
    walsh_courses.append(upcoming_course)
walsh_courses.sort()

# Print the message first, then each course in the list
print("\nThis is my course of study with upcoming courses added:")
for course in walsh_courses:
    print(course)

# ---------- Requirement 4 ----------
# Remove each course I've already taken and keep track of what was removed
removed_courses = []
for course in courses_already_taken:
    walsh_courses.remove(course)
    removed_courses.append(course)

# Print the message first, then each removed course
print("\nI do not have to take these courses:")
for course in removed_courses:
    print(course)

# ---------- Requirement 5 ----------
# Print the courses left, each on its own line, under the message
print("\nI plan to take the following courses next term")
for course in walsh_courses:
    print(course)

# ---------- Requirement 6 ----------
# Numbers from 1 to 1000 that are divisible by 6 (start at 6, step by 6, stop before 1001)
divisible_by_six = list(range(6, 1001, 6))

# ---------- Requirement 7 ----------
# Print the first 20 numbers, each on its own line
print("\nHere are twenty numbers divisible by 6.")
for number in divisible_by_six[:20]:
    print(number)

# ---------- Requirement 8 ----------
# Find the maximum of the original large list and store it
max_number = max(divisible_by_six)

# ---------- Requirement 9 ----------
print("\nThe maximum value in the list is: " + str(max_number))

# ---------- Requirement 10 ----------
# Sum the values from the 10th item to the 50th item, including both ends.
# The 10th item is at index 9, and the slice stops before index 50, so it includes the 50th item.
sum_of_values = sum(divisible_by_six[9:50])
print("Here is the sum of several values in the list: " + str(sum_of_values))

# ---------- Requirement 11 ----------
# Overwrite the original course list variable with the large list of numbers
walsh_courses = divisible_by_six
