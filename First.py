def find_median():
  """
  Finds the median of user-provided marks.
  """

  # Get number of students
  num_students = int(input("Enter the number of students: "))

  # Initialize list to store marks
  marks = []

  # Get marks for each student
  for i in range(num_students):
    mark = int(input(f"Enter mark for student {i+1}: "))
    marks.append(mark)

  # Sort the marks
  sorted_marks = sorted(marks)

  # Calculate and display median based on even/odd student count
  if len(sorted_marks) % 2 == 1:
    median = sorted_marks[len(sorted_marks) // 2]
    print(f"The median mark is: {median}")
  else:
    mid_index = len(sorted_marks) // 2
    median = (sorted_marks[mid_index - 1] + sorted_marks[mid_index]) / 2
    print(f"The median mark is: {median}")

# Run the function
find_median()
