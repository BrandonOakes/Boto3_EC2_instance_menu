import boto3
from helper_functions import input_n_clear

def main_menu():
    ''''Main menu options for user'''
    while True:
        try:
            user_choice = int(input_n_clear(
'''Welcome to Easy EC2!

Please enter the number below depending on your desired option:

1) Start my ec2 instance
2) Stop my ec2 instance
3) Exit

:'''))
            if user_choice in [1,2,3]:
                return user_choice
            else:
                print("Invalid option! Enter 1,2 or 3\n")
        except Exception as e:
            print("Invalid input:", e, "\n")
