import boto3
from helper_functions import clear

def user_instance():
    '''Creates boto3 session and  ec2 instance object
       from user input'''

     #get IAM user

    iam_user = input("Enter your Identity Access Management user profile: ")

    clear()
    #get to AWS management console

    aws_console = boto3.session.Session(profile_name=iam_user)

    #get to ec2 web service console

    ec2_resource = aws_console.resource('ec2')

    #get instance id

    ec2_id = input("Enter the EC2 instance Id you would like to look up: ")

    clear()

    #get specified ec2 instance

    ec2_instance = ec2_resource.Instance(id=ec2_id)

    return ec2_instance


def instance_current_state(instance):
    '''returns instance running state'''

    #get ec2 instance state

    ec2_state = instance.state

    #get name of ec2 instance state (state will return a dictionary)

    ec2_state_name = ec2_state['Name']

    return ec2_state_name

def display_current_state(instance):
    '''Outputs the current ec2 instance state'''

    ec2_state_name = instance_current_state(instance)

    print(f"Current ec2 instance state: {ec2_state_name}")

def start_instance(instance):

    ec2_state_name = instance_current_state(instance)

    if ec2_state_name == 'running':
        print("You are good to go, your instance was already running")

    else:
        instance.start()
        print("Your instance is starting up....one moment")
        instance.wait_until_running()
        print(f"Current ec2 instance state: {instance.state['Name']}")

def stop_instance(instance):

    ec2_state_name = instance_current_state(instance)

    if ec2_state_name == 'stopped':
        print("You are good to go, your instance was already stopped")

    else:
        instance.stop()
        print("Your instance is stopping....one moment")
        instance.wait_until_stopped()
        print(f"Current ec2 instance state: {instance.state['Name']}")
