import boto3
from helper_functions import input_n_clear

def user_instance():
    '''Creates boto3 session and ec2 instance object
       from user input'''
    iam_user = input_n_clear('''Enter your Identity Access Management user
                                profile: ''')
    aws_console = boto3.session.Session(profile_name=iam_user) #AWS management console object
    ec2_resource = aws_console.resource('ec2') #AWS ec2 object
    ec2_id = input_n_clear('''Enter the EC2 instance Id you would like to
                              look up: ''')
    ec2_instance = ec2_resource.Instance(id=ec2_id) #get specified ec2 instance
    return ec2_instance


def instance_current_state(instance):
    '''returns instance running state'''
    ec2_state = instance.state  #get ec2 instance state
    ec2_state_name = ec2_state['Name'] #get name of ec2 instance state (state will return a dictionary)
    return ec2_state_name


def display_current_state(instance):
    '''Outputs the current ec2 instance state'''
    ec2_state_name = instance_current_state(instance)
    print(f"Current ec2 instance state: {ec2_state_name}")


def start_instance(instance):
    ''' Starts instance or lets user know instance is already running'''
    ec2_state_name = instance_current_state(instance)
    if ec2_state_name == 'running':
        print("You are good to go, your instance was already running")
    else:
        instance.start()
        print("Your instance is starting up....one moment")
        instance.wait_until_running()
        print(f"Current ec2 instance state: {instance.state['Name']}")


def stop_instance(instance):
    ''' Stops instance or lets user know instance is already stopped'''
    ec2_state_name = instance_current_state(instance)
    if ec2_state_name == 'stopped':
        print("You are good to go, your instance was already stopped")
    else:
        instance.stop()
        print("Your instance is stopping....one moment")
        instance.wait_until_stopped()
        print(f"Current ec2 instance state: {instance.state['Name']}")
