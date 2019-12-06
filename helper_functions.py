import os

def clear():
    '''Clears command line screen after each input question'''
    os.system('cls' if os.name=='nt' else 'clear')

def input_n_clear(input_question):
    '''custom input function - takes user input and
       then clears command line'''
    input(input_question)
    clear()
