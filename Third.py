def find_younger_person(name1, dob1, name2, dob2):
  """
  Compares the dates of birth and names of two people to find the younger one.

  Args:
    name1: First person's name (capitalized string).
    dob1: First person's date of birth (DD-MM-YYYY string).
    name2: Second person's name (capitalized string).
    dob2: Second person's date of birth (DD-MM-YYYY string).

  Returns:
    The name of the younger person (capitalized string).
  """

  # Extract day, month, and year from date of birth strings
  day1, month1, year1 = map(int, dob1.split("-"))
  day2, month2, year2 = map(int, dob2.split("-"))

  # Compare dates: year first, then month, then day
  if year1 < year2:
    return name1
  elif year1 > year2:
    return name2
  elif month1 < month2:
    return name1
  elif month1 > month2:
    return name2
  elif day1 < day2:
    return name1
  elif day1 > day2:
    return name2
  else:  # Same date of birth, compare names alphabetically
    return name1 if name1 < name2 else name2

# Get input data for both persons
name1 = input("Enter first person's name: ").capitalize()
dob1 = input("Enter first person's date of birth (DD-MM-YYYY): ")
name2 = input("Enter second person's name: ").capitalize()
dob2 = input("Enter second person's date of birth (DD-MM-YYYY): ")

# Find and print the younger person's name
younger_person = find_younger_person(name1, dob1, name2, dob2)
print("The younger person is:", younger_person)
