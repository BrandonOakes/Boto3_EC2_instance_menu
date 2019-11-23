import boto3

def main_menu():
    ''''Main menu options'''

    user_choice = int(input('''
Welcome to Easy EC2!

Please enter the number below depending on your desired option:

1) Start my ec2 instance
2) Stop my ec2 instance
3) Exit

:'''))
    return user_choice
