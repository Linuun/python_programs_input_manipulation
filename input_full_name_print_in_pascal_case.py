# ask user to input their full name in incorrect casing
full_name = input("Enter your full name (in incorrect casing): ")
# print the input in pascal case
print("Your name in pascal case is", '' .join(word.capitalize() for word in full_name.split()))