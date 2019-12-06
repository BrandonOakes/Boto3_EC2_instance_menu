import boto3
from helper_functions import input_n_clear
from instance_session import display_current_state, instance_current_state \
                             start_instance, stop_instance, user_instance
from menu_options import main_menu

user_choice = main_menu()
if user_choice == 3:
    quit()
ec2_instance = user_instance() #get ec2 instance object
display_current_state(ec2_instance) #get name of ec2 instance state (state will return a dictionary)
if user_choice == 1:
    start_instance(ec2_instance)
elif user_choice ==2:
    stop_instance(ec2_instance)
