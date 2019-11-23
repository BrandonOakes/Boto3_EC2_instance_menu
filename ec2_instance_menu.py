import boto3
from instance_session import user_instance, instance_current_state
from instance_session import display_current_state, start_instance, stop_instance
from menu_options import main_menu
from helper_functions import clear


user_choice = main_menu()

clear()

if user_choice == 3:

    quit()

#get ec2 instance object

ec2_instance = user_instance()

#get name of ec2 instance state (state will return a dictionary)

display_current_state(ec2_instance)

if user_choice == 1:

    start_instance(ec2_instance)

elif user_choice ==2:

    stop_instance(ec2_instance)
