user_name = input("Enter your username: ")
password = input("Enter your password: ")
password_length = len(password)
cryptic_password = password_length * '*'
print(f'{user_name}, Your password {cryptic_password} is {password_length} letters long')
