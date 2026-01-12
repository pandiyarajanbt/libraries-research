import secrets
import string

# def generate_secure_number(length):
#     characters = string.ascii_letters + string.digits + string.punctuation
#     random_number = ''.join(secrets.choice(characters) for _ in range(length))
#     return random_number

# length = 6
# response = generate_secure_number(length)
# print(response)


# import random

# random_numbers = random.randint(1, 10)
# print(random_numbers, "random_numbers")


def generate_secure_number(numbers):
    random_numbers = int("".join(str(secrets.choice(numbers)) for _ in range(5)))
    return random_numbers

response = generate_secure_number(numbers=[
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9
])

print("Your Otp", response)

def vaild_otp(respose):
    users_otp = int(input("Enter Your Otp : "))
    
    if response == users_otp:
        return True
    
    else:
        return False
    
response = vaild_otp(response)

print("OTP STATUS :", response)
