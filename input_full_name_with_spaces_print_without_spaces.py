# ask user to input their full name with space characters at the beginning
full_name = input("Enter your full name (put spaces at the beginning): ")
# print the input with no spaces at the beginning
print("Your full name is", full_name.lstrip())