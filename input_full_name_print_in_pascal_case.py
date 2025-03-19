# ask user to input their full name
full_name = input("Enter your full name: ")
# print the input in pascal case
print("Your name in pascal case is", '' .join(word.capitalize() for word in full_name.split()))