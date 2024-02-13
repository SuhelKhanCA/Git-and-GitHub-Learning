def sort_string():
  """
  Prompts user for a string, converts it to lowercase, sorts alphabetically, and prints the sorted string.
  """
  
  # Get input string from user
  user_string = input("Enter a string: ")

  # Convert the string to lowercase
  lowercase_string = user_string.lower()

  # Sort the characters alphabetically
  sorted_string = ''.join(sorted(lowercase_string))

  # Print the sorted string
  print("The sorted string is:", sorted_string)

# Run the function
sort_string()
