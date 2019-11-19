import boto3

#get IAM user

iam_user = input("Enter your Identity Access Management user profile: ")

#get to AWS management console

aws_console = boto3.session.Session(profile_name=iam_user)

#get to ec2 web service console

ec2_resource = aws_console.resource('ec2')

#get instance id

ec2_id = input("Enter the EC2 instance Id you would like to look up: ")

#get specified ec2 instance

ec2_instance = ec2_resource.Instance(id=ec2_id)

#get ec2 instance state

ec2_state = ec2_instance.state

#get name of ec2 instance state (state will return a dictionary)

ec2_state_name = ec2_state['Name']

#print ec2 instance state

print(f"Current ec2 instance state: {ec2_state_name}")

if ec2_state_name == 'running':
    ec2_action = input("Do you want to stop your instance?\n(Yes/No): ").lower()
    if ec2_action == 'yes':
        ec2_instance.stop()
        print("Your instance is stopping....one moment")
        ec2_instance.wait_until_stopped()
        print(f"Current ec2 instance state: {ec2_instance.state['Name']}")
    else:
        print("Hope this script was helpful, have a nice day")

elif ec2_state_name == 'stopped':
    ec2_action = input("Do you want to start your instance?\n(Yes/No): ").lower()
    if ec2_action == 'yes':
        ec2_instance.start()
        print("Your instance is starting up....one moment")
        ec2_instance.wait_until_running()
        print(f"Current ec2 instance state: {ec2_instance.state['Name']}")
    else:
        print("Hope this script was helpful, have a nice day")
