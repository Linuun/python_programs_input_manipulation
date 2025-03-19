# ask user to input their full name in incorrect casing
full_name = input("Enter your full name (in incorrect casing): ")
# print the input in snake case
print("Your name in snake case is", '_' .join(word.lower() for word in full_name.split()))